import face_recognition
from sklearn import svm
from sklearn.metrics import accuracy_score
import os
import cv2
import pickle

def facerec(path):
    
    clf = pickle.load(open('imageupload/model.sav', 'rb'))
    result = ""
    test_image = face_recognition.load_image_file(path)
    result="false"
    # Find all the faces in the test image using the default HOG-based model
    face_locations = face_recognition.face_locations(test_image)
    print(face_locations)
    no = len(face_locations)
    print("Number of faces detected: ", no)
    if no!=1:
        result="false"
    else:
        # Predict all the faces in the test image using the trained classifier
        for i in range(no):
            test_image_enc = face_recognition.face_encodings(test_image)[i]
            name = clf.predict([test_image_enc])
            column_number = clf.predict_proba([test_image_enc]).shape[1]
            print(column_number)
            for i in range(column_number):
                prob = clf.predict_proba([test_image_enc])[:,i][0]
                print(prob)
                if (prob>.4):
                    result=name[0]
    print(result)
                
    return result
