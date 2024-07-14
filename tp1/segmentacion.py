import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from utils.utils import load_image, plot_images, plot_images_comparison, change_rgb2hsv

Imagen_a_segmentar = [load_image('enunciado/segmentacion.png')]

def nothing(x):
    pass

# Crear una ventana con deslizadores para seleccionar el rango de color
cv.namedWindow('Rango de color')

# Crear deslizadores para el rango de color
cv.createTrackbar('H min', 'Rango de color', 0, 179, nothing)
cv.createTrackbar('H max', 'Rango de color', 179, 179, nothing)
cv.createTrackbar('S min', 'Rango de color', 0, 255, nothing)
cv.createTrackbar('S max', 'Rango de color', 255, 255, nothing)
cv.createTrackbar('V min', 'Rango de color', 0, 255, nothing)
cv.createTrackbar('V max', 'Rango de color', 255, 255, nothing)

# Convertir la imagen de RGB a BGR
image = cv.cvtColor(Imagen_a_segmentar[0], cv.COLOR_RGB2BGR)

while True:
    # Convertir la imagen de BGR a HSV en cada iteración del bucle
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    # Leer los valores de los deslizadores
    h_min = cv.getTrackbarPos('H min', 'Rango de color')
    h_max = cv.getTrackbarPos('H max', 'Rango de color')
    s_min = cv.getTrackbarPos('S min', 'Rango de color')
    s_max = cv.getTrackbarPos('S max', 'Rango de color')
    v_min = cv.getTrackbarPos('V min', 'Rango de color')
    v_max = cv.getTrackbarPos('V max', 'Rango de color')
    
    # Crear una máscara con el rango de color seleccionado
    mask = cv.inRange(hsv, (h_min, s_min, v_min), (h_max, s_max, v_max))
    
    # Aplicar la máscara a la imagen original
    result = cv.bitwise_and(image, image, mask=mask)
    
    # Mostrar la imagen con la máscara aplicada
    cv.imshow('Rango de color', result)
    
    # Salir del bucle si se presiona la tecla 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas
cv.destroyAllWindows()
