import numpy as np
import cv2 as cv
import os
from PIL import Image, ImageDraw
from collections import defaultdict
from math import sqrt, pi, cos, sin

im = np.array(Image.open("/Users/tobieabel/Desktop/Ball/ball001.jpg"))
#im[:,:,[1,2,]] = 0 #turn individual channel up or down (0 = black)


#binarise each colour channel based on the values for the red ball
#np_img_boolean = np.logical_and(im[:,:,[0]] > 100,im[:,:,[1]] < 70,im[:,:,[2]] < 70)#using a comparison operator on a ndarray creates a new array of boolean values

np_img_bin = np.empty([480,640,1])#create empty ndarray
#replace empty array value with 1 or 1.25 depending on pixel value matching logical_and condition
np_img_bin[:,:,:] = np.where((np.logical_and(im[:,:,[0]] > 100,im[:,:,[1]] < 70,im[:,:,[2]] < 70)),1.25,1)
#apply 1.25 to relevant pixels on original image for red channel only. Need to apply max score of 255
np_img_bins = np.clip((im[:,:,[0]] * np_img_bin),0,255)
#add values from original image to the green and blue channels
for i in range(1,3):
    np_img_bins = np.insert(np_img_bins,i,im[:,:,i],axis = 2)#inserts before indicies 1, value im[:,:,i], along axis 2

#alternatively use this to simply turn 'true' pixels to 255 (white), and everything else stays at black
#np_img_bin[:,:,:]= np_img_boolean * 255#iterate through the boolean array and multiply each element by 255.  True = 1 and False = 0 so only 'True' elements are multiplied

#get trim version of one of the balls for analysis
np_img_trim = np_img_bins[270:335,247:314,:]#ymin:ymax,xmin:xmax
print (np_img_bin.shape)
print(type(np_img_trim))
im_new = Image.fromarray(np.uint8(np_img_bins))
im_new.show()



#detect the edges using
input_pixels = im_new.load()#not sure why but i need to load() the PIL image to access its pixel values
width, height = im_new.width, im_new.height

#create output image
output_image = Image.new("RGB",im_new.size)
draw = ImageDraw.Draw(output_image)

#first, convert to greyscale (could use PIL library or CV for this too)
intensity = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        intensity[x, y] = sum(input_pixels[x, y]) / 3
keep = []
# then compute convolution between intensity and kernels
for x in range(1, im_new.width - 1):
    for y in range(1, im_new.height - 1):
        magx = intensity[x + 1, y] - intensity[x - 1, y]#Calculate the difference between the pixels above and below
        magy = intensity[x, y + 1] - intensity[x, y - 1]#and to the left and right of each pixel

        # Draw in black and white the magnitude
        color = int(sqrt(magx ** 2 + magy ** 2))
        if color > 25:
            draw.point((x, y), (color, color, color))
            keep.append((x,y))
output_image.show()
#output_image.save("edge.png")

# Find circles
rmin = 30
rmax = 40
steps = 100
threshold = 0.85

points = []#an array containing the radius, offset of x and ofset of y for each possible circle
for r in range(rmin, rmax + 1):
    for t in range(steps):
        points.append((r, int(r * cos(2 * pi * t / steps)), int(r * sin(2 * pi * t / steps))))

acc = defaultdict(int)
for x, y in keep:#iterate through all edges, offset by value from Points[] and store number of times those values occur in acc dictionary
    for r, dx, dy in points:
        a = x - dx
        b = y - dy
        acc[(a, b, r)] += 1

circles = []
for k, v in sorted(acc.items(), key=lambda i: -i[1]):#iterate through all possible circles in acc dict and keep only those over the threshold, and whose centre is outside other circles(to avoid too many circles)
    x, y, r = k
    if v / steps >= threshold and all((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2 for xc, yc, rc in circles):
        print(v / steps, x, y, r)
        circles.append((x, y, r))

draw_result = ImageDraw.Draw(output_image)

np_img_final = np.zeros((im.shape))#create blank array
#np_img_final = np.array(output_image)#or copy of array showing edges

for x, y, r in circles:#loop through the list of circle, and draw on the output image
    draw_result.ellipse((x-r, y-r, x+r, y+r), outline=(255,0,0,0))
    np_img_ball = im[(y-r):(y+r), (x-r):(x+r), :]#also cut those coordinates from the originl image
    np_img_final[(y-r):(y+r), (x-r):(x+r),:] = np_img_ball#and paste them to the blank/edge image

output_image.show()

im_final = Image.fromarray(np.uint8(np_img_final))
im_final.show()