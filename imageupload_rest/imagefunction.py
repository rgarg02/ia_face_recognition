#when the user posts an image this function should run
import cv2
import os
import numpy as np
def image(path):
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (0, 0, 0)
    detector = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #trainingData.yml is my pretrained model which includes a unique id for each user
    recognizer.read('recognizer/trainingData.yml')
    im = cv2.imread(path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if 2 < conf < 125:
            cv2.putText(im, str(Id), (x, y + h),fontface, fontscale, fontcolor)
    cv2.imshow('Recognition', im)
    cv2.imwrite("image.jpg",im)
    cv2.waitKey(0)
    res = "yes"
    return res
    

