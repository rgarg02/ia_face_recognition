import face_recognition
from sklearn import svm
import os
import cv2
# Training the SVC classifier

# The training data would be all the face encodings from all the known images and the labels are their names
encodings = []
names = []

def add(path,Id):
    cam = cv2.VideoCapture(path)
    print(path)
    sampleNum = 0
    error=0
    detector = cv2.CascadeClassifier(
        'imageupload/cascades/data/haarcascade_frontalface_default.xml')
    while True:
        try:
            ret, img = cam.read()
            frame = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            image = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            if faces.size==0:
                print("non")
            else:
                error-=1
                print(error)
                sampleNum = sampleNum + 1
                pat = "imageupload/dataSet/" + str(Id)+"/"
                try:
                    os.makedirs(pat)
                except OSError:
                    print("Creation of the directory %s failed" % pat)
                else:
                    print("Successfully created the directory %s" % pat)
                cv2.imwrite(pat + str(sampleNum) + ".jpg",image)
                cv2.imshow('frame', image)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                    # break if the sample number is morethan 20
                elif sampleNum > 10:
                    cv2.destroyAllWindows()
                    break
        except Exception:
            error+=1
            if error>20:
                break
                return "No face found"
            
    if sampleNum==11:
        cam.release()
        getImagesID()
        return "User Added"
    elif sampleNum==0:
        cam.release()
        cv2.destroyAllWindows()
        return "Face Not Found"
    else:
        cam.release()
        cv2.destroyAllWindows()
        shutil.rmtree(pat)
        return "Error: Need longer video for better accuracy"
    
# Training directory
def getImagesID():
    print("training...")
    import pickle
    traindir = os.listdir('imageupload/dataSet/')

    for person in traindir:
        pix = os.listdir("imageupload/dataSet/" + person)

    # Loop through each training image for the current person
        for person_img in pix:
            # Get the face encodings for the face in each image file
            face = face_recognition.load_image_file("imageupload/dataSet/" + person + "/" + person_img)
            face_bounding_boxes = face_recognition.face_locations(face)

            #If training image contains none or more than faces, print an error message and exit
            if len(face_bounding_boxes) != 1:
                exit()
            else:
                face_enc = face_recognition.face_encodings(face)[0]
                # Add face encoding for current image with corresponding label (name) to the training data
                encodings.append(face_enc)
                names.append(person)

    # Create and train the SVC classifier
    clf = svm.SVC(gamma='scale',probability=True)
    print("fit starting")
    clf.fit(encodings,names)
    pickle.dump(clf, open('imageupload/model.sav', 'wb'))
