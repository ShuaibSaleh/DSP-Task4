import cv2
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift, fftfreq,  ifftshift, ifft2
import numpy as np

# # plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

# img_c1 = cv2.imread("left01.jpg", 0)
# # img_c2 = fft2(img_c1)
# # img_c3 = fftshift(img_c2)
# # img_c4 = ifftshift(img_c3)
# # img_c5 = ifft2(img_c4)

# plt.imshow(img_c1, "gray"), plt.title("Original Image")
# # plt.subplot(152), plt.imshow(np.log(1+np.abs(img_c2)), "gray"), plt.title("Spectrum")
# # plt.subplot(153), plt.imshow(np.log(1+np.abs(img_c3)), "gray"), plt.title("Centered Spectrum")
# # plt.subplot(154), plt.imshow(np.log(1+np.abs(img_c4)), "gray"), plt.title("Decentralized")
# # plt.subplot(155), plt.imshow(np.abs(img_c5), "gray"), plt.title("Processed Image")

# plt.show()