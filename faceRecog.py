from cnn import CNN
import network
from random import randint
import numpy as np
import cv2
import os
import tensorflow as tf
from getFace import *

hdf5 = "/media/zac/easystore/dataset.hdf5"
# batches = readFromHDF5(hdf5, 100, 10)

# print(batches)

# file = tables.open_file(hdf5, mode='r')
network = CNN(.0000001, (224, 224), 140, 128)
# totalBatch = file.root.trainImg.shape[0] // network.batchSize
# testBatch = file.root.testImg.shape[0] // network.batchSize
# file.close()
# # # print(getClassfierCount("alligned_db/aligned_images_DB"))
gpu_options = tf.GPUOptions(allow_growth=True)
with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
    #178
    network.train(sess, 33, 33, 100)

# print(batches

    # 10 faces
    # 0.14424242424242426 0
    # 0.14424242424242426 10
    # 0.14454545454545453 20
    # 0.14484848484848484 30
    # 0.14484848484848484 40
    # 0.14515151515151514 50
    # 0.14515151515151514 60
    # 0.14606060606060606 70
    # 0.1478787878787879  90
    # 0.14939393939393938 110
    # 0.1481818181818182  130
    # 0.14727272727272728 140
    # 0.1478787878787879  150 
    # 0.14878787878787877 160
    # 0.14939393939393938 170
    # 0.14939393939393938 180
    # 0.1496969696969697  190
    # 0.1506060606060606  200
    # 0.1506060606060606  210
    # 0.1506060606060606  220
    # 0.1503030303030303  230
    # 0.15121212121212121 240
    # 0.1509090909090909  250
    # 0.15121212121212121 260
    # 0.15121212121212121 270
    # 0.1509090909090909  280
    # 0.15151515151515152 290
    # 0.15181818181818182 300
    # 0.15212121212121213 310
    # 0.15181818181818182 330
    # 0.15242424242424243 350
    # 0.15181818181818182 370
    # 0.15121212121212121 380
    # 0.15212121212121213 390
    # 0.15242424242424243 400
    # 0.1509090909090909  410
    # 0.15121212121212121 420
    # 0.15454545454545454 440


    # 0.1687878787878788  0
    # 0.17                20
    # 0.1684848484848485  40
    # 0.16545454545454547 60
    # 0.16484848484848486 80
    # 0.16303030303030303 100

    # 0.17303030303030303 0
    # 0.17212121212121212 10
    # 0.17212121212121212 30
    # 0.17181818181818181 50
    # 0.17242424242424242 70
    # 0.17272727272727273 80
    # 0.17333333333333334 100
    # 0.1778787878787879  300
    # 0.18                700


