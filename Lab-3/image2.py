import cv2

image = cv2.imread('cat.jpg')
print(image.shape)
image = cv2.resize(image, (300, 500))
cv2.imshow('THE CAT', image)
cv2.waitKey(0)
cv2.destroyAllWindows()