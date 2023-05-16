#OpenCV2
import cv2


#Class to detect faces
class Detector():

    #Constructor
    def __init__(self,
                 face_cascade_dir:str = r'.\data\haarcascade_frontalface_alt.xml') -> None:
        self.model = cv2.CascadeClassifier()
        self.model.load(face_cascade_dir)
    

    #Method to detect faces
    def detect_faces(self, image):
        faces = self.model.detectMultiScale(image)
        if len(faces)!=0:
            for i,face in enumerate(faces):
                (x,y,w,h)=face
                image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
                image = cv2.putText(image, f"Face {i}", (x,y), color = (0,255,0))
            return image
        else:
            return image