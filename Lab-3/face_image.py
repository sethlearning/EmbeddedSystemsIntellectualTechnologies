import cv2
import sys

# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt2.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalcatface.xml')
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalcatface_extended.xml')

# image = cv2.imread('images/cat.jpg')
# image = cv2.imread('images/cats2.jpg')
# image = cv2.resize(cv2.imread('images/people.jpg'), (0,0), fx=0.5, fy=0.5)
# image = cv2.resize(cv2.imread('images/people2.jpg'), (0,0), fx=0.5, fy=0.5)

if (len(sys.argv) < 2):
    file = 'images/people.jpg'
else:
    file = sys.argv[1]

if (len(sys.argv) < 3):
    face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt2.xml')
else:
    face_cascade = cv2.CascadeClassifier(sys.argv[2])

image = cv2.imread(file)

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grayimage, 1.3, 5)

for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0), 2)
    # roi_gray = grayimage[y:y+h, x:x+w]
    # roi_color = image[y:y+h, x:x+w]
    
cv2.imshow('Face', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
