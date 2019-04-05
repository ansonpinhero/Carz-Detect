from ObjectDetector import Detector
import io

from flask import Flask, render_template, request
from flask import jsonify
from PIL import Image
from flask import send_file


app = Flask(__name__)

detector = Detector()


# detector.detectNumberPlate('twocar.jpg')



@app.route("/", methods=['POST'])
def upload():
    if request.method == 'POST':
        file = Image.open(request.files['file'].stream)
        
        j = detector.detectObject(file)
        
        return j


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)