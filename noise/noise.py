import cv2
from scipy.linalg import svd
import numpy as np

img = "InitialImage.jpg"

img = cv2.imread(img)

gaussian_noise = np.random.normal(0, 50, img.shape)

noisy_img = cv2.add(img, gaussian_noise.astype(np.uint8))

cv2.imwrite('image_back.jpg', noisy_img)