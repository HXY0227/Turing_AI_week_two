import cv2
import numpy as np
image = cv2.imread('image.png')
swapped_image = image.copy()
swapped_image[:, :, [0, 2]] = image[:, :, [2, 0]]
cv2.imshow('Original Image', image)
cv2.imshow('Swapped Channels Image', swapped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('swapped_image.png', swapped_image)