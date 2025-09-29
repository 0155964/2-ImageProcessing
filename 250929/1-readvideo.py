import cv2
video = cv2.VideoCapture('image/光伏发电预测讲解 2.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
print('fps:',fps)
print('the video size:',height,width)

while video.isOpened():
    ret, frame = video.read()
    cv2.imshow('video',frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()