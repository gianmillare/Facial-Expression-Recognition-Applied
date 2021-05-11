# Dependencies
from tensorflow.keras.models import model_from_json
from tensorflow.python.keras.backend import set_session
import numpy as np
import tensorflow as tf

# Set appropriate memory (optional)
config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.15
session = tf.compat.v1.Session(config=config)
set_session(session)

# Create the class that will hold the model
class FacialExpressionModel(object):

    # list of emotions/expressions
    EMOTIONS_LIST = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

    # define the init method
    def __init__(self, model_json_file, model_weights_file):

        # load the model from the json model
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        # load the weights that is saved in the same directory (model_weights.h5)
        self.loaded_model.load_weights(model_weights_file)
        # self.loaded_model._make_predict_function()
    
    # function to predict the emotions/expressions
    def predict_emotion(self, img):
        
        # Create a session
        global session
        set_session(session)
        
        # Make predictions on the loaded model
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]