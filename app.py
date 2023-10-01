from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from prediction.predict import DogCat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        #so here it will take our input images
        self.filename = "inputImage.jpg"
        #in this class only we do prediction
        self.classifier = DogCat(self.filename)

#here it goes to the home page
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    #it gets the input image
    image = request.json['image']
    #decodes the image by calling the decodeImage function
    decodeImage(image, clApp.filename)
    #calling the prediction function to predict
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)




if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)

