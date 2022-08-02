import cv2
import keras 
import tensorflow as tf
import numpy as np

# image_keras = keras.utils.load_img('.\\data\\images_dataset\\1.jpg')
# image_keras = keras.utils.img_to_array(image_keras)
# print('keras one', image_keras)

# image_cv = cv2.imread('.\\data\\images_dataset\\1.jpg')
# image_cv = image_cv[...,::-1].astype(np.float32)
# print('cv one', image_cv)

net = cv2.dnn.readNetFromTensorflow(".\\model\\saved_model.pb")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow("Mahjong Tile Detector", frame)
    cv2.waitKey(1)