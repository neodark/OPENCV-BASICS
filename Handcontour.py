import cv2

img = cv2.imread("hand.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 50, 140)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Numbers of contours are : ", len(contours))
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow("final", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
