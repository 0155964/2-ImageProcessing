import cv2
image1 = cv2.imread('image/eye-4.jpg',0)
image2 = image1

#相加超过255取模所以比较暗
result = image1+image2
#cv2.add()使用保留为255，所以比较亮
result2 = cv2.add(image1, image2)

cv2.imshow('image',image1)
cv2.imshow('image+image',result)
cv2.imshow('cv2.add()',result2)

cv2.waitKey(0)
cv2.destroyAllWindows()