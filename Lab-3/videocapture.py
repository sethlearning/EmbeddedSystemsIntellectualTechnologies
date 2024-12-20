import cv2

capture = cv2.VideoCapture(0)
if (capture.isOpened == False):
    print('Can\'t open.')

# capture.set(3, 500)
# capture.set(4, 300)

while (capture.isOpened):
    success, image = capture.read()
    if (image is None):
        break
    cv2.imshow('Camera', image)
    if (cv2.waitKey(25) == ord('q')):
        break

capture.release()
cv2.destroyAllWindows()
