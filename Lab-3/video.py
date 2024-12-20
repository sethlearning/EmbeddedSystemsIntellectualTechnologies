import cv2
video = cv2.VideoCapture('aliens_trim.mp4')
while True:
    success, image = video.read()
    cv2.imshow('Video', image)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break