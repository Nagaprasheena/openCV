import os
import uuid
from flask import Blueprint, current_app, render_template, request, redirect, url_for, send_from_directory, flash, jsonify
from werkzeug.utils import secure_filename

from .services.processing import process_image_from_path, list_operations

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


ui_bp = Blueprint('ui', __name__)
api_bp = Blueprint('api', __name__)


@ui_bp.route('/')
def index():
    ops = list_operations()
    return render_template('index.html', operations=ops)


@ui_bp.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        flash('No file part provided')
        return redirect(url_for('ui.index'))

    file = request.files['image']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('ui.index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_id = str(uuid.uuid4())
        name, ext = os.path.splitext(filename)
        saved_name = f"{input_id}{ext}"
        input_path = os.path.join(current_app.config['UPLOAD_FOLDER'], saved_name)
        file.save(input_path)

        # Operation and params
        operation = request.form.get('operation', 'grayscale')
        params = {k: v for k, v in request.form.items() if k not in ['operation']}

        try:
            output_filename = f"{input_id}.png"
            output_path = os.path.join(current_app.config['RESULTS_FOLDER'], output_filename)

            result = process_image_from_path(
                input_path=input_path,
                output_path=output_path,
                operation=operation,
                params=params,
                base_dir=current_app.config['BASE_DIR']
            )
        except Exception as e:
            current_app.logger.exception('Processing failed')
            flash(f'Processing failed: {e}')
            return redirect(url_for('ui.index'))

        return redirect(url_for('ui.result', result_id=input_id))

    flash('Unsupported file type')
    return redirect(url_for('ui.index'))


@ui_bp.route('/result/<result_id>')
def result(result_id: str):
    output_filename = f"{result_id}.png"
    output_path = os.path.join(current_app.config['RESULTS_FOLDER'], output_filename)
    if not os.path.exists(output_path):
        flash('Result not found')
        return redirect(url_for('ui.index'))
    return render_template('result.html', result_id=result_id, image_url=url_for('ui.get_result_file', filename=output_filename))


@ui_bp.route('/results/<path:filename>')
def get_result_file(filename):
    return send_from_directory(current_app.config['RESULTS_FOLDER'], filename)


@ui_bp.route('/uploads/<path:filename>')
def get_upload_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


@ui_bp.route('/download/<result_id>')
def download_result(result_id: str):
    output_filename = f"{result_id}.png"
    return send_from_directory(current_app.config['RESULTS_FOLDER'], output_filename, as_attachment=True)


@api_bp.route('/operations', methods=['GET'])
def api_operations():
    return jsonify(list_operations())


@api_bp.route('/process', methods=['POST'])
def api_process():
    # JSON API: expects {"image_path": str (optional if file provided), "operation": str, "params": {...}}
    operation = request.form.get('operation') or (request.json and request.json.get('operation'))
    params = (request.json and request.json.get('params')) or {}

    input_path = None
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            input_id = str(uuid.uuid4())
            name, ext = os.path.splitext(secure_filename(file.filename))
            saved_name = f"{input_id}{ext}"
            input_path = os.path.join(current_app.config['UPLOAD_FOLDER'], saved_name)
            file.save(input_path)
    if not input_path:
        input_path = request.json and request.json.get('image_path')

    if not input_path or not operation:
        return jsonify({"error": "image or operation missing"}), 400

    output_filename = f"{uuid.uuid4()}.png"
    output_path = os.path.join(current_app.config['RESULTS_FOLDER'], output_filename)

    try:
        result = process_image_from_path(
            input_path=input_path,
            output_path=output_path,
            operation=operation,
            params=params,
            base_dir=current_app.config['BASE_DIR']
        )
    except Exception as e:
        current_app.logger.exception('Processing failed')
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "result_path": url_for('ui.get_result_file', filename=output_filename, _external=True),
        "local_result_filename": output_filename
    })
