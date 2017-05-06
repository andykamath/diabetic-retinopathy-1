from PIL import Image
from matplotlib import pyplot as plt
from scipy.misc import imread, imresize
from scipy.signal import medfilt
from skimage.morphology.selem import disk
from scipy.ndimage.morphology import grey_closing
from math import sqrt
import numpy as np
import cv2

def resizeretina(retinaRGB, x, y):
	a = float(np.shape(retinaRGB)[0])
	b = float(np.shape(retinaRGB)[1])
	print a, b
	retinaRGB = imresize(retinaRGB, sqrt(x * y / (a * b)))
	return retinaRGB

def getopticdiscartifacts(retinaRGB, closingThresholdValue, opticDiscDilationSize, artifactMinSize):
	I = retinaRGB/255.0
	I = sum(I, 3) / 3
	I = medfilt(I)
	I = np.histogram(I)
	se = disk(8)
	closeI = grey_closing(I, se)
retinaRGB = imread('/home/andy/DROOP/images/test/original/20051019_38557_0100_PP.tif');
retinaRGB = resizeretina(retinaRGB, 752, 500)

closingThresholdValue = 0.64
opticDiscDilationSize = 4
artifactMinSize = 1100

getopticdiscartifacts(retinaRGB, closingThresholdValue, opticDiscDilationSize, artifactMinSize)