# openvino-cpp-object-detection
C++ inference pipeline using OpenVINO for object detection using intel CPU or GPU on COCO dataset images with JSON output.

# OpenVINO C++ Object Detection

This project demonstrates a C++ inference pipeline using OpenVINO for object detection on COCO dataset images.

## Features

- OpenVINO model loading
- Real-time image inference
- Bounding box visualization
- Detection result export to JSON

## Technologies

- C++
- OpenVINO
- OpenCV
- COCO Dataset

Model sourced from Intel OpenVINO Open Model Zoo.

openvino-cpp-object-detection
│
├── models
│   ├── model.xml
│   └── model.bin
│
├── images
│   └── sample.jpg
│
├── src
│   ├── main.cpp
│   ├── inference.cpp
│   ├── postprocess.cpp
│
├── include
│   ├── inference.hpp
│   └── postprocess.hpp
│
├── output
│   ├── results.json
│   └── output_image.jpg
│
├── CMakeLists.txt
└── README.md


## Model Preparation

pip install -r requirements.txt

python scripts/prepare_model.py

This project uses the **YOLOv4 Tiny TensorFlow model** from the OpenVINO Open Model Zoo.

The model was downloaded and converted to OpenVINO IR format (`.xml` and `.bin`) using the Open Model Zoo model tools.

### 1. Clone Open Model Zoo

git clone https://github.com/openvinotoolkit/open_model_zoo.git

### 2. Install dependencies

pip install openvino-dev
pip install tensorflow

### 3. Download the model

cd open_model_zoo/tools/model_tools

python downloader.py --name yolo-v4-tiny-tf

### 4. Convert the model to OpenVINO IR

python converter.py --name yolo-v4-tiny-tf

### 5. Output

The converted model files will be generated in:

open_model_zoo/tools/model_tools/public/yolo-v4-tiny-tf/FP16/

Files generated:

* yolo-v4-tiny-tf.xml
* yolo-v4-tiny-tf.bin

### Notes

* TensorFlow must be installed before running the converter because the model is a TensorFlow `.pb` graph.
* The Model Optimizer requires Python 3.8–3.10.
* If OpenVINO runtime is installed separately, ensure the Python environment contains `openvino-dev` for model conversion tools.
