import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import os, sys
from tqdm import tqdm
from random import shuffle
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
IMAGE_SIZE= 200
model=load_model('potmodel.h5')
path = "/home/subhash123/project/test/"
dirs = os.listdir( path )
count =1
# This would print all the files and directories
for imagename in dirs:
	#file=file.split(".")i
	#if(len(file)==2 and file[1]=="jpg"):
	print("image number processing")
	print(count)
	print(imagename)
	#pre.main(path,imagename)
	count+=1
	img = cv2.imread(path+imagename)
	img = cv2.resize(img,(IMAGE_SIZE,IMAGE_SIZE))
	img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
	m=model.predict([img])[0]
	print(m)
	if(m[0]>m[1]):
		print("potato\n")
	elif(m[0]<m[1]):
		print("weed\n")