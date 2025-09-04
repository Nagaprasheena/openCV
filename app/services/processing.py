import os
from typing import Dict, Any, List
import cv2
import numpy as np


# Utility: parse numeric params safely

def _to_int(val: Any, default: int) -> int:
    try:
        return int(val)
    except Exception:
        return default


def _to_float(val: Any, default: float) -> float:
    try:
        return float(val)
    except Exception:
        return default


def _read_image(path: str):
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Unable to read image at {path}")
    return img


def _ensure_dir(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)


# Exposed operations list (name, label, params schema)

def list_operations() -> List[Dict[str, Any]]:
    return [
        {"name": "grayscale", "label": "Grayscale", "params": []},
        {"name": "blur", "label": "Gaussian Blur", "params": [{"name": "ksize", "label": "Kernel Size (odd)", "type": "int", "default": 5}]},
        {"name": "canny", "label": "Canny Edge", "params": [
            {"name": "threshold1", "label": "Threshold 1", "type": "int", "default": 100},
            {"name": "threshold2", "label": "Threshold 2", "type": "int", "default": 200}
        ]},
        {"name": "threshold", "label": "Binary Threshold", "params": [
            {"name": "thresh", "label": "Threshold", "type": "int", "default": 127},
            {"name": "maxval", "label": "Max Value", "type": "int", "default": 255}
        ]},
        {"name": "equalize_hist", "label": "Histogram Equalization (Gray)", "params": []},
        {"name": "convert_hsv", "label": "Convert to HSV", "params": []},
        {"name": "convert_lab", "label": "Convert to LAB", "params": []},
        {"name": "split_merge", "label": "Split & Merge channels (Swap R/B)", "params": []},
        {"name": "bitwise_not", "label": "Bitwise NOT", "params": []},
        {"name": "resize", "label": "Resize", "params": [
            {"name": "scale", "label": "Scale", "type": "float", "default": 0.5}
        ]},
        {"name": "rotate", "label": "Rotate", "params": [
            {"name": "angle", "label": "Angle (deg)", "type": "float", "default": 90}
        ]},
        {"name": "smooth_bilateral", "label": "Bilateral Filter", "params": [
            {"name": "d", "label": "Diameter", "type": "int", "default": 9},
            {"name": "sigmaColor", "label": "Sigma Color", "type": "int", "default": 75},
            {"name": "sigmaSpace", "label": "Sigma Space", "type": "int", "default": 75}
        ]},
        {"name": "mask_circle", "label": "Mask Circle", "params": []},
        {"name": "sobel", "label": "Sobel Gradients", "params": []},
        {"name": "laplacian", "label": "Laplacian", "params": []},
        {"name": "contours", "label": "Find Contours", "params": []},
        {"name": "face_detect", "label": "Face Detection (Haar)", "params": [
            {"name": "scaleFactor", "label": "Scale Factor", "type": "float", "default": 1.1},
            {"name": "minNeighbors", "label": "Min Neighbors", "type": "int", "default": 5}
        ]},
    ]


# Core processing entry point

def process_image_from_path(input_path: str, output_path: str, operation: str, params: Dict[str, Any], base_dir: str) -> str:
    img = _read_image(input_path)
    op = operation.lower()

    if op == 'grayscale':
        out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif op == 'blur':
        k = _to_int(params.get('ksize'), 5)
        if k % 2 == 0: k += 1
        out = cv2.GaussianBlur(img, (k, k), 0)
    elif op == 'canny':
        t1 = _to_int(params.get('threshold1'), 100)
        t2 = _to_int(params.get('threshold2'), 200)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        out = cv2.Canny(gray, t1, t2)
    elif op == 'threshold':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        th = _to_int(params.get('thresh'), 127)
        mv = _to_int(params.get('maxval'), 255)
        _, out = cv2.threshold(gray, th, mv, cv2.THRESH_BINARY)
    elif op == 'equalize_hist':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        out = cv2.equalizeHist(gray)
    elif op == 'convert_hsv':
        out = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif op == 'convert_lab':
        out = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    elif op == 'split_merge':
        b, g, r = cv2.split(img)
        out = cv2.merge([r, g, b])
    elif op == 'bitwise_not':
        out = cv2.bitwise_not(img)
    elif op == 'resize':
        s = _to_float(params.get('scale'), 0.5)
        out = cv2.resize(img, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    elif op == 'rotate':
        angle = _to_float(params.get('angle'), 90)
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        out = cv2.warpAffine(img, M, (w, h))
    elif op == 'smooth_bilateral':
        d = _to_int(params.get('d'), 9)
        sc = _to_int(params.get('sigmaColor'), 75)
        ss = _to_int(params.get('sigmaSpace'), 75)
        out = cv2.bilateralFilter(img, d, sc, ss)
    elif op == 'mask_circle':
        mask = np.zeros(img.shape[:2], dtype='uint8')
        (h, w) = img.shape[:2]
        r = min(h, w) // 4
        center = (w // 2, h // 2)
        cv2.circle(mask, center, r, 255, -1)
        out = cv2.bitwise_and(img, img, mask=mask)
    elif op == 'sobel':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
        out = cv2.convertScaleAbs(cv2.magnitude(sobelx, sobely))
    elif op == 'laplacian':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lap = cv2.Laplacian(gray, cv2.CV_64F)
        out = cv2.convertScaleAbs(lap)
    elif op == 'contours':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        out = img.copy()
        cv2.drawContours(out, cnts, -1, (0, 255, 0), 2)
    elif op == 'face_detect':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Locate haar cascade provided in the repo
        cascade_candidates = [
            os.path.join(base_dir, 'Leraning_opencv', 'haar_face.xml'),
            os.path.join(base_dir, 'haar_face.xml')
        ]
        cascade_path = next((p for p in cascade_candidates if os.path.exists(p)), None)
        if not cascade_path:
            raise FileNotFoundError('haar_face.xml not found in project')
        haar_cascade = cv2.CascadeClassifier(cascade_path)
        scaleFactor = _to_float(params.get('scaleFactor'), 1.1)
        minNeighbors = _to_int(params.get('minNeighbors'), 5)
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
        out = img.copy()
        for (x, y, w, h) in faces_rect:
            cv2.rectangle(out, (x, y), (x+w, y+h), (0, 255, 0), 2)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    # Ensure 3-channel before save to PNG when needed
    if out.ndim == 2:
        out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)

    _ensure_dir(output_path)
    ok = cv2.imwrite(output_path, out)
    if not ok:
        raise RuntimeError('Failed to write output image')

    return output_path
