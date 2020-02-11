from flask import request
import flask
from flask import send_file
import werkzeug
from imageai.Detection import ObjectDetection

app = flask.Flask(__name__)

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5") 
detector.loadModel()

@app.route('/', methods = ['POST', 'GET'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    imagefile.save(filename)
    location = flask.request.files['json']
    jsonfile = werkzeug.utils.secure_filename(location.filename)
    location.save(jsonfile)

    print("\nReceived image File name : " + imagefile.filename)

    detections = detector.detectObjectsFromImage(input_image="androidFlask.jpg", output_image_path="imagenew.jpg", thread_safe=True) 
    results = ''
    for eachObject in detections:
        results = results + ' ' + eachObject["name"]
    if(results == ''): results = 'No object detected'
    return results

app.run(host = '0.0.0.0', port=5000, debug=True, threaded=False)
