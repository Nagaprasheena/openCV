import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Config
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
    app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32 MB upload limit

    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['BASE_DIR'] = base_dir
    app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, 'uploads')
    app.config['RESULTS_FOLDER'] = os.path.join(base_dir, 'results')

    # Ensure folders exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

    # Register blueprints
    from app.routes import ui_bp, api_bp
    app.register_blueprint(ui_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
