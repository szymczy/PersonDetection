from detection import detection
from flask import Flask, request, abort
import cv2
import numpy as np

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

app = Flask(__name__)


@app.route('/obrazki', methods=['POST'])
def upload_file():
    image_file = request.files['image']
    validate_file(image_file)
    img_np = create_image_from_bytes(image_file)
    number_of_faces, time = detection(img_np)
    return f'Number of people on image: {number_of_faces}, time taken: {time}'


def validate_file(image_file):
    extension = image_file.filename.split('.')[-1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        abort(400, "Extension not allowed")


def create_image_from_bytes(image_file):
    byte_str = b''
    for byte in image_file.stream:
        byte_str += byte
    nparr = np.frombuffer(byte_str, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
