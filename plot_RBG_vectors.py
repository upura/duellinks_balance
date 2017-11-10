#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot RGB vectors with KMeans results
"""

import os
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img_dirs = ['img']
CARD_NUM = 4
CLASS_NUM = 3
img_data = []

def convertImgToRGB(img):
    for card in range(CARD_NUM):
        trim_img = img[1180:1200,(80 + 113 * card):(193 + 113 * card)]
        averages = trim_img.mean(0).mean(0)
        img_data.append(list(averages))

def imgImport():
    for i, d in enumerate(img_dirs):
        files = os.listdir('./'+d)    
        for f in files:
            img = cv2.imread('./' + d + '/' + f)
            convertImgToRGB(img)

def plotRGBVectors(img_data):
    pred = KMeans(n_clusters = CLASS_NUM).fit_predict(img_data)
    x = []
    y = []
    z = []
    for i in range(len(pred)):
        x.append(img_data[i][0])
        y.append(img_data[i][1])
        z.append(img_data[i][2])
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_xlim(0, 256)
    ax.set_ylim(0, 256)
    ax.set_zlim(0, 256)
    ax.scatter(x, y, z, "o", c=pred)
    plt.show()

imgImport()
plotRGBVectors(img_data)
