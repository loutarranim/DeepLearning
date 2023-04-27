import os
from flask import Flask, render_template, jsonify
from algorithm.object_detector import YOLOv7
from utils.detections import draw
import cv2
import json
import urllib.request
import numpy as np

app = Flask(__name__)
@app.route('/')
def home():
    url = "car_white.jpg"
    image = cv2.imread(url) 
    yolov7 = YOLOv7()
    yolov7.set(ocr_classes=['number_plate'])
    yolov7.load('best.weights', classes='classes.yaml', ocr_weights='best', device='cpu') 
    # use 'gpu' for CUDA GPU inference
    detections = yolov7.detect(image)
    detected_image = draw(image, detections)
    response_data = {'detections': detections}
    return render_template('index.html', response_data=json.dumps(response_data))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)