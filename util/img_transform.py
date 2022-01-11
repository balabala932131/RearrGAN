import cv2
import random
import numpy as np

def rotate(img,angle):#angle=[-180:180]
    cols, rows=img.shape[:2]
    M=cv2.getRotationMatrix2D((rows/2,cols/2),angle,1)
    img_T = cv2.warpAffine(img,M,(rows,cols))
    return img_T

def gamma(img, gamma):#gamma[0.5,1.5]
    invGamma = 1.0/gamma
    img=np.array(img).astype("uint8")
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype("uint8")
    return cv2.LUT(img, table)

def randcut(img,shuffle_list): #[B,C,H,W]
    a=shuffle_list
    h,w,c=img.shape
    imgnew=np.zeros_like(img)
    size=int(h/2)
    blocks=[]
    for i in range(2):
        for j in range(2):
            blocks.append(img[size*i:size*(i+1),size*j:size*(j+1),:])

    c=0
    for m in range(2):
        for n in range(2):
            imgnew[size*m:size*(m+1),size*n:size*(n+1),:]=blocks[a[c]]
            c=c+1
    return imgnew