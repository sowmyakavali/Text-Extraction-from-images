import cv2
import os

def pre_process(path ):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    alpha = 1.5 # Contrast control (1.0-3.0)
    beta = 45 # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
    return adjusted

