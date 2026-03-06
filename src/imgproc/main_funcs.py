import os
import sys
import cv2
import glob
import inspect
import numpy as np
from scipy.optimize import curve_fit
from scipy.ndimage import center_of_mass
from scipy.spatial import KDTree



def read_img(path):
    # Reading images
    try:
      if path[-4:] == '.txt':
        img = np.loadtxt(path)
      else:
        img = np.array(PIL.Image.open(path))
    except:
      print('ERROR: Something went wrong while image reading!!!')
    return img


def img_proj(img):
  # Image projections
  hor_proj = np.sum(img,0)
  vrt_proj = np.sum(img,1)
  return hor_proj, vrt_proj


def movmean_1d(ar, _n=5):
    # Moving average/mean
    return np.convolve(ar, np.ones(_n)/_n, mode='same')
