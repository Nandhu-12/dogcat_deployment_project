import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class DogCat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        # model = load_model(os.path.join("model", "model_vgg16.h5"))
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        #loading the image
        # test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.load_img(imagename, target_size = (64,64))
        #converting to numpy array
        test_image = image.img_to_array(test_image)
        #applying expand dimensions
        test_image = np.expand_dims(test_image, axis = 0)
        #predicting with argmax operation
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'dog'
            return [{ "image" : prediction}]
        else:
            prediction = 'cat'
            return [{ "image" : prediction}]


