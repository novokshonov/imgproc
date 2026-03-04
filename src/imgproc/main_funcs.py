import numpy as np
from scipy.optimize import curve_fit


def img_proj(img):
  # Image projections
  hor_proj = np.sum(img,0)
  vrt_proj = np.sum(img,1)
  return hor_proj, vrt_proj
