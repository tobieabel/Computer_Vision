from PIL import Image
import numpy as np
import cv2
import scipy
import imutils
from imutils import perspective
#Perform histogram equalisation,  which should normalise image intensity and increase contrast
im=np.array(Image.open("/Users/tobieabel/Desktop/Ball Test/ball001.jpg").convert('L'))
imhist,bins = np.histogram(im.flatten(),256,normed=True)
cdf = imhist.cumsum()
cdf = 255 * cdf/cdf[-1]
im2 = np.interp(im.flatten(),bins[:-1],cdf)
im2 = im2.reshape(im.shape)
new_img = Image.fromarray(np.uint8(im2))
new_img.show()
print(im2.shape)
#Load the images
#image = cv2.imread("/Users/tobieabel/Desktop/Ball Test/ball003.jpg")
#output = image.copy()


#convert the image to binary balck and white.  You can play around with the threshold values
#ret, image = cv2.threshold(image, 100, 255, 0)

#grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY )
#canny = cv2.Canny(grey,100,150)
#circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 0.8, 20)#detect spheres and circles in image
#if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
#	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
#	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
#		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
#		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#cv2.imshow("output", np.hstack([image, output]))

#grey and blur image slightly


#ret, image = cv2.threshold(image, 150, 150, 150)
#image = cv2.GaussianBlur(image,(7,7),0)
#perform edge detection and then perform dilation and erosion to close gaps between edges
#image = cv2.Canny(image,50,100)
#image = cv2.dilate(image, None, iterations=1)
#image = cv2.erode(image,None,iterations=1)
#kernel = np.ones((7, 23), np.uint8)
#image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


#cv2.imshow("image",canny)
#cv2.waitKey(10000)
