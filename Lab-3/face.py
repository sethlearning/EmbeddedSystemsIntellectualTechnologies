import cv2
import sys

# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt2.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalcatface.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalcatface_extended.xml')

# capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture('videos/aliens_trim.mp4')
# capture = cv2.VideoCapture('videos/cats.mp4')
# capture = cv2.VideoCapture('videos/cats_faces.mp4')

if (len(sys.argv) < 2):
    capture = cv2.VideoCapture(0)
else:
    capture = cv2.VideoCapture(sys.argv[1])

if (len(sys.argv) < 3):
    face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt2.xml')
else:
    face_cascade = cv2.CascadeClassifier(sys.argv[2])

while True:
    ret, image = capture.read()
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayimage, 1.3, 5)

    for x,y,w,h in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0), 2)
        # roi_gray = grayimage[y:y+h, x:x+w]
        # roi_color = image[y:y+h, x:x+w]
    
    cv2.imshow('Face', image)
    # if( cv2.waitKey(30) & 0xFF == ord('q')):
    if( cv2.waitKey(1) & 0xFF == ord('q')):
        break

capture.release()
cv2.destroyAllWindows()
