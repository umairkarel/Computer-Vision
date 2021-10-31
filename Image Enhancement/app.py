import cv2

# Reading Image
img = cv2.imread('imgs/img2.png')

# Converting to grayScale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resizing
imgResize = cv2.resize(imgGray, (600, 600))

# Adaptive Thresholding
output = cv2.adaptiveThreshold(src=imgResize, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=29, C=5)

cv2.imwrite('imgs/output.jpg', output)
cv2.imshow("Original", imgResize)
cv2.imshow("Image", output)
cv2.waitKey(0)