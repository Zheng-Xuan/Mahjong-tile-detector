import cv2
import keras 
import numpy as np

# Read in the classes
with open("classes.txt", 'r') as f:
    classes = f.read().split()

# Load model
model = cv2.dnn.readNet(model= "frozen_models/frozen_graph.pb", framework= "Tensorflow")

# Initiate camera
cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, img = cap.read()

    blob = cv2.dnn.blobFromImage(img, size= (320, 240), swapRB= True, scalefactor= 1/255)

    model.setInput(blob)

    output = model.forward()

    prediction = np.argsort(output[0])[::-1][0]

    cv2.putText(img, text= classes[prediction], org= (5, 25), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale= 0.7, color= (0, 255, 0), thickness= 2)

    cv2.imshow("Mahjong tile detection", img)
    cv2.waitKey(1)
