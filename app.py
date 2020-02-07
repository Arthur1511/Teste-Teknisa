import cv2
from flask import Flask, render_template, request
import numpy as np
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        img = request.files.get('imagem')
        img_format = secure_filename(img.filename.split(".")[1])
        img_name = 'img.' + img_format
        img_path = './img/' + img_name
        img.save(img_path)

        imagem = cv2.imread(img_path)

        classification = "haarcascade_frontalface_default.xml"

        faceCascade = cv2.CascadeClassifier(classification)

        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imwrite("./static/" + img_name, imagem)

        return render_template('result.html', path="./static/" + img_name)


if __name__ == '__main__':
    app.run()
