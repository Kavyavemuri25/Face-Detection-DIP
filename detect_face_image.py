import cv2
from werkzeug.utils import secure_filename
from PIL import Image
import os

upload_dir = 'img/'
allowed_images = set(['png', 'jpg','PNG','JPG','jpeg'])

def face_detect(file):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if file and checkImage(file.filename):
        file_path = uploadImage(file)
    img = cv2.imread(file_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

def checkImage(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_images

def uploadImage(file):
    file_path = upload_dir + secure_filename(file.filename)
    file.save(file_path)
    return file_path
