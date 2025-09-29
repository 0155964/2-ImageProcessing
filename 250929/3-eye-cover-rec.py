# 打码区域坐标: x1=186, x2=278, y1=172, y2=219

import cv2
import numpy as np



image= cv2.imread('image/eye-4.jpg')
y1,y2=172,219
x1,x2=186,278
rec=np.random.randint(0,256,(y2-y1,x2-x1,3),dtype=np.uint8)
image[y1:y2,x1:x2]=rec
cv2.imshow('random',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

height, width, channels = image.shape
print(f"图像尺寸: 高度={height}, 宽度={width}, 通道数={channels}")