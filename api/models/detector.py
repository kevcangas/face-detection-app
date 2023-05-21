#OpenCV2
import cv2


#Class to detect faces
class Detector():

    #Constructor
    def __init__(self,
                 face_cascade_dir:str = r'api\models\data\haarcascade_frontalface_alt.xml') -> None:
        self.model = cv2.CascadeClassifier()
        self.model.load(face_cascade_dir)
    

    #Method to detect faces
    def detect_faces(self, image):
        image_processed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.model.detectMultiScale(image_processed)
        if len(faces)!=0:
            for i,face in enumerate(faces):
                (x,y,w,h)=face
                image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
                image = cv2.putText(img = image, 
                                    text = f"Face {i}", 
                                    org = (x,y-5), 
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=0.5, 
                                    color = (0,255,0)
                                    )
            return image
        else:
            return image