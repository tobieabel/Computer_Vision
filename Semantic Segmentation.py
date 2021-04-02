#Create png mask images for training semantic segmentation.  Creates one class for all balls
#and puts multiple balls on a single png so there is one png per jpg training image

import os
import cv2
import json
import numpy as np

source_folder = "/Users/tobieabel/Desktop/Ball_Test"
to_save_folder = "/Users/tobieabel/Desktop/Ball_TestSeg/"
json_path = "/Users/tobieabel/Desktop/Ball_Test_json/VGG.json"
MASK_WIDTH = 480  # Dimensions should match those of ground truth image
MASK_HEIGHT = 640

# Read JSON file
with open(json_path) as f:
    data = json.load(f)

# Extract X and Y coordinates if available and update dictionary
for itr in data:
    file_name_png = data[itr]["filename"][:-3] + 'png'
    all_points = []
    mask = np.zeros((MASK_WIDTH, MASK_HEIGHT))#black mask
    for i in range (len(data[itr]["regions"])): #for each region, i.e. each ball
            x_points = data[itr]["regions"][str(i)]["shape_attributes"]["all_points_x"]
            y_points = data[itr]["regions"][str(i)]["shape_attributes"]["all_points_y"]
            for it, x in enumerate(x_points):#for each region go thorugh the x and y points and add them to a list
                all_points.append([x, y_points[it]])
            arr = np.array(all_points, 'int32')#turn the list into an nd array
            cv2.fillPoly(mask, ([arr]), color=(100))#and paste that nd array on the mask
            arr = 0#clear lists and arrays before processing next region
            all_points = []
    cv2.imwrite(os.path.join(to_save_folder, file_name_png), mask)#save the mask to a new image


#from PIL import Image


#their_frame = Image.open('/Users/tobieabel/Downloads/ADE_train_00000001.png')
#np_their_frame = np.array(their_frame.getdata())
#print (np.amax(np_their_frame))
#my_frame = Image.open('/Users/tobieabel/Desktop/Ball_TestSeg/Whiteball1001.png')
#np_my_frame = np.array(my_frame.getdata())
#print (np.amax(np_my_frame))
#print('end')



