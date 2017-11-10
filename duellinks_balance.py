#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cv2
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

img_dirs = ['img']
CARD_NUM = 4
CLASS_NUM = 3
img_data = []

def convertImgToRGB(img):
    for card in range(CARD_NUM):
        trim_img = img[1180:1200,(80 + 113 * card):(193 + 113 * card)]
        averages = trim_img.mean(0).mean(0)
        img_data.append(averages)

def imgImport():
    for i, d in enumerate(img_dirs):
        files = os.listdir('./'+d)    
        for f in files:
            img = cv2.imread('./' + d + '/' + f)
            convertImgToRGB(img)

def createBarplot(counter):
    labels = []
    cnts = []
    for label, cnt in counter.most_common():
        labels.append(label)
        cnts.append(cnt)
    left = np.array([(i+1) for i in range(len(cnts))])
    height = np.array(cnts)
    plt.bar(left, height, tick_label=labels, align="center")

def converRGBToCollection(img_data):
    pred = KMeans(n_clusters = CLASS_NUM).fit_predict(img_data)
    pred.resize(int(len(pred)/CARD_NUM), CARD_NUM)
    pred = list(pred)
    for i in range(len(pred)):
        pred[i].sort()
        pred[i] = str(pred[i])
    counter = Counter(pred)
    createBarplot(counter)

imgImport()
converRGBToCollection(img_data)
