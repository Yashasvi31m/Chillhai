import cv2

image = cv2.imread(r"C:\Users\yashu\Downloads\scenery.jpg")
Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image.shape,Gray.shape)
canny1 = cv2.Canny(Gray,200,10)
canny2 = cv2.Canny(Gray,200,170)

cv2.imshow("Canny1",canny1)
cv2.imshow("Canny2",canny2)
cv2.waitKey(3000)
