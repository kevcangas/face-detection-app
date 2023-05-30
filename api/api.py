#Extarnal libraries
import cv2
import numpy as np
import base64


#Models
from api.models.detector import Detector


#FastAPI
from fastapi import APIRouter, UploadFile
from fastapi import Path, Body, File


api = APIRouter()
ver = '/v1'


@api.post("/imagefaces/")
def upload_file(file: UploadFile = File(...)):
    #Read file content
    contents = file.file.read()
    
    #Decoding image
    decode_img = cv2.imdecode(np.frombuffer(contents, np.uint8), -1)
    file.file.close()

    #Detecting faces in the image
    img_faces = Detector().detect_faces(decode_img)
    img_faces = cv2.resize(decode_img,[400,300])
    img_faces = cv2.imencode('.png',img_faces)[1]
    

    #Coding image
    byte_img = base64.b64encode(img_faces)


    return {
        "detail": {
            "filename": file.filename,
            "image": byte_img
            }
    }