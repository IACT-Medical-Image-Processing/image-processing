import numpy as np
from cv2 import imread
from matplotlib import pyplot as plt

img = imread('../images/img1.jpg',0)
 
hist,bins = np.histogram(img.flatten(),256,[0,256])
 
cdf = hist.cumsum()
cdf_normalized = cdf *hist.max()/ cdf.max() # this line not necessary.
 
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]

# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from __future__ import division, print_function
# import sys
# import os
# import cv2
# import numpy as np

# def hist_eq(img):
#     data = img.copy().flatten()
#     hist, bins = np.histogram(data, 256, density=True)
#     cdf = hist.cumsum()
#     cdf = 255*cdf/cdf[-1]
#     img_eq = np.interp(data, bins[:-1], cdf)
#     return img_eq.reshape(img.shape)

# def main(argv):
#     if len(argv) < 2:
#         print("usage: {} IMAGE".format(argv[0]))
#         return 1
#     image_path = argv[1]
#     image_name, _ = os.path.splitext(os.path.basename(image_path))
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     img_eq = hist_eq(img)
#     if not cv2.imwrite("equalized_{}.png".format(image_name), img_eq):
#         return 1
#     return 0

# if __name__ == "__main__":
#     main(sys.argv)