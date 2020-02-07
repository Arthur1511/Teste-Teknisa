import cv2

classification = "haarcascade_frontalface_default.xml"

# Setando a classificacao do xml da OpenCV para olhos
faceCascade = cv2.CascadeClassifier(classification)

image = cv2.imread("0.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Fazer a deteccao da imagem
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Setar o retangulo azul
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Exibir a imagem
cv2.imshow("Titulo da imagem", image)
cv2.waitKey(0)
