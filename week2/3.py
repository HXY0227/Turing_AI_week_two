import cv2
import numpy as np

background = cv2.imread('image2.png')
slider = cv2.imread('slider.png')

bg_height, bg_width = background.shape[:2]
slider_height, slider_width = slider.shape[:2]

start_x = bg_width // 2
roi = background[0:bg_height, start_x:bg_width]

result = cv2.matchTemplate(roi, slider, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left_roi = max_loc
top_left_original = (top_left_roi[0] + start_x, top_left_roi[1])
bottom_right_original = (top_left_original[0] + slider_width, top_left_original[1] + slider_height)

background[top_left_original[1]:bottom_right_original[1],
           top_left_original[0]:bottom_right_original[0]] = slider

cv2.imwrite('result.png', background)
cv2.imshow('Result', background)
cv2.waitKey(0)
cv2.destroyAllWindows()