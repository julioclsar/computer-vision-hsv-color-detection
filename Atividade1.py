import cv2 as cv
import numpy as np

cap = cv.VideoCapture (0)

while True:

    _, ImgCap = cap.read()

    imgHSV = cv.cvtColor(ImgCap, cv.COLOR_BGR2HSV)
    res = cv.inRange(imgHSV, (160, 100, 100), (200, 255, 255))

    medias = cv.mean(ImgCap)

    cores = ['azul', 'verde', 'vermelho']
    cor_predom = cores[np.argmax(medias[:3])]
    print(f"Cor predominante: {cor_predom}")

    cv.imshow('destaque', res)

    tecla = cv.waitKey(1)
    if tecla == ord("s"):
        break