#https://www.dropbox.com/s/th0u3mpsl71fxit/CertificateTemplate.jpg
#PIL--python image library

from PIL import Image, ImageDraw, ImageFont
img=Image.open("./CertificateTemplate.jpg")

import matplotlib.pyplot as plt
import numpy as num 

def print_img(img):
    plt.imshow(num.array(img))
    plt.show()

#cv2--computer vision 2

import cv2

img=cv2.imread("./CertificateTemplate.jpg")

def generate_certificate(img,name="Enter name"):
    generated_img=img.copy()
    font=cv2.FONT_HERSHEY_SIMPLEX
    coordinates=(700,750)
    font_size=3.5
    font_color= (51,51,51)
    font_thickness= 10
    cv2.putText(generated_img,name,coordinates,font,font_size,font_color,
                font_thickness)
    return generated_img

def save_img(img,name):
    path="./certi_{}.jpg". format(name)
    print(cv2.imwrite(path,img))
    
generated_img=generate_certificate(img,"Ritika")
save_img(generated_img,"Ritika")
