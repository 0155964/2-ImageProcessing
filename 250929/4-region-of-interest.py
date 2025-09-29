import cv2
image= cv2.imread('image/eye-4.jpg')

roi=image[100:300,100:300]
cv2.imshow('image',image)
cv2.imshow('roi',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()