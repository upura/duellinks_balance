#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2

IMG_SIZE = 28 # 画像の1辺の長さ
COLOR_CHANNELS = 3 # RGB
IMG_PIXELS = IMG_SIZE * IMG_SIZE * COLOR_CHANNELS # 画像のサイズ*RGB

img_dirs = ['img']
img_data = []
img_label = []

for i, d in enumerate(img_dirs):
    # ./img/以下の各ディレクトリ内のファイル名取得
    files = os.listdir('./'+d)
    for f in files:
        img = cv2.imread('./' + d + '/' + f)
#        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
#        img = img.flatten().astype(np.float32)/255.0
        img_data.append(img)