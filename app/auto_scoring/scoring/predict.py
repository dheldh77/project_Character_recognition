import os
import tensorflow as tf
import numpy as np
import sys
from imageResizing import PostProcessingWithoutLabel


class Predict:
    def __init__(self):
        self.__MODEL_PATH = './model'
        self.__MODEL_NAME = '3C3D_model.h5'
        self.__MODEL_PATH = os.path.join(self.__MODEL_PATH, self.__MODEL_NAME)
        self.model = self.load_model()

    def load_model(self):
        model = tf.keras.models.load_model(self.__MODEL_PATH)
        return model

    def predict(self, path):
        predict_data = PostProcessingWithoutLabel(path)
        predict_data = predict_data.astype(np.float32).reshape(1, 28, 28, 1)
        predict_number = np.argmax(self.model.predict(predict_data))
        # print(predict_number)
        return predict_number

def Predict_object(x):
    predict = Predict()
    # print(x)
    ans = predict.predict(x)
    return ans
# predict = Predict()
# predict.predict('./data/predict/001/01.png')
# predict.predict('./data/predict/001/02.png')
# predict.predict('./data/predict/001/03.png')

# MODEL_PATH = './model'
# predict_number = 8
# MODEL_NAME = '3C3D_model_' + str(predict_number) + '.h5'
# MODEL_PATH = os.path.join(MODEL_PATH, MODEL_NAME)
#
# try:
#     model = tf.keras.models.load_model(MODEL_PATH)
# except FileNotFoundError:
#     print(MODEL_PATH + ': File not found')
#     sys.exit()
#
# def predict_model(number, data):
