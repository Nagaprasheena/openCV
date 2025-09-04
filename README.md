# openCV

## Learning OpenCV

This repository contains code and resources related to learning OpenCV. OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.

### Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Directory Structure](#directory-structure)
4. [Usage](#usage)
5. [Contributing](#contributing)

### Introduction
OpenCV is a powerful library aimed at real-time computer vision. This repository provides various examples and tutorials to help you get started with OpenCV.

### Installation
To use the code in this repository, you need to have OpenCV installed. You can install it using pip:

```bash
pip install opencv-python
```

### Directory Structure
The repository is organized into the following directories:

* Image Processing: Contains code related to various image processing techniques, such as filtering, transformations, and color space conversions.
* Video Processing: Includes scripts for video analysis and manipulation, such as reading, writing, and processing video frames.
* Feature Detection: Implements different feature detection algorithms, including edge detection, corner detection, and blob detection.
* Object Detection: Examples of object detection using OpenCV, including face detection, pedestrian detection, and more.

### Usage
To get started with the examples, clone the repository:

```bash
git clone https://github.com/JaswanthSanapala/openCV.git
cd openCV
```
Navigate to the desired directory and run the Python scripts. Each directory contains a README file with specific instructions and explanations for the included examples.

#### Run the Web App (Flask UI)
This repository also includes a Flask-based UI that wraps common OpenCV operations (grayscale, blur, canny, thresholding, histogram equalization, gradients, transformations, masking, smoothing, contours, and face detection using the included Haar cascade file `Leraning_opencv/haar_face.xml`).

1. Create and activate a virtual environment (recommended):
   - Windows (PowerShell)
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - macOS/Linux
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. Open your browser to:
   - http://127.0.0.1:5000/

5. Usage notes:
   - Upload an image (PNG/JPG/JPEG/WEBP/BMP), select an operation, adjust parameters, and process.
   - Results are saved in the `results/` folder. Uploaded files are saved in `uploads/`.
   - For face detection, the app uses the `Leraning_opencv/haar_face.xml` cascade file.

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.
