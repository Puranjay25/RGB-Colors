import cv2 as cv
import numpy as np 

def onchange(x):
	pass

window=np.zeros((300,512,3), np.uint8)
cv.namedWindow('RGB Colors')

cv.createTrackbar('B','RGB Colors', 0, 255, onchange)
cv.createTrackbar('G', 'RGB Colors', 0, 255, onchange)
cv.createTrackbar('R', 'RGB Colors', 0, 255, onchange)

flag='On/Off'
cv.createTrackbar(flag, 'RGB Colors', 0, 1, onchange)

while True:
	cv.imshow('RGB Colors',window)

	k = cv.waitKey(1) 

	if k==27:
		break

	b=cv.getTrackbarPos('B','RGB Colors')
	g=cv.getTrackbarPos('G','RGB Colors')
	r=cv.getTrackbarPos('R','RGB Colors')
	f=cv.getTrackbarPos(flag,'RGB Colors')

	if f==0:
		window[:]=0

	else:
		window[:]=[b,g,r]

cv.destroyAllWindows()