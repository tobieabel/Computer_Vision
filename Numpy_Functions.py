from PIL import Image
import numpy as np
import os
import json
import xmltodict
jpgsource = "/Users/tobieabel/Desktop/Ball_Test"
#Open all jpeg files in a directory and turn into ndarrays
images = [i for i in os.listdir(jpgsource)if i != ".DS_Store"]#list comprehension to create list of file names ina directory
images_list = {}#need to do this as a dictionary so you still have the file name as key
for i in images:#iterate through the list of names and open each as ndarray as uint8 with shape height, width and 3 for channels
    np_img_test = np.array(Image.open(jpgsource + '/' + i))
    images_list[i] = np_img_test
#open all xml files and turn in ndarrays, including multiple bboxes, need to rearrange xmin and ymin values and turn into %
xml_list = []
xml_list_2 = []
gt_boxes = []
xmlsource = "/Users/tobieabel/Desktop/BallXML_Test"
xml_files = [i for i in os.listdir(xmlsource)if i != ".DS_Store"]
#for i in xml_files:
#    with open(xmlsource + '/' + i,"r")as f:
#        data_dict = xmltodict.parse(f.read())#this turns xml into a dictionary
#        for xy in (data_dict['annotation']['object']['bndbox']).values():#check the xml file to see structure.  This code only works with xml files with multiple balls
#            xml_list.append(int(xy)/1000)#tf expects floating point so divide x by image width and y by image height
#        xml_list_2.append(xml_list)#The tensor has to be a list containing a list containing tensors, hense two lists
#        np_xml = np.array(xml_list_2,dtype = np.float32)
#        gt_boxes.append(np_xml)
#        xml_list = []#clear list before next file in loop
#        xml_list_2 = []#clear before next file in loop

#print(data_dict['annotation']['object']['bndbox'])
#open jpeg as PIL image and convert to Greyscale(L)
#img = Image.open("/Users/tobieabel/Desktop/Ball/ball001.jpg")#.convert("L")
#img2 = Image.open("/Users/tobieabel/Desktop/Ball/Yellowball200729.jpg")
#print(type(img))
#convert to NP Array
#np_img = np.array(img)
#np_img2 = np.array(img2)
#print(np_img[400,300]) #y = 400, x = 300.  Display RGB values of pixel at that location
#make copies, changing the Green and Blue and then Red and Blue pixels to 0, then concatenate to one image
#np_img_R = np_img.copy()
#np_img_R[:,:,(1,2)] = 0
#np_img_G = np_img.copy()
#np_img_G[:,:,(0,2)] = 0
#np_img_con = np.concatenate((np_img_R, np_img_G),axis=1)
#inverse the image.  Numpy automatically applies the 255 -  action to each element of the np_img array
#np_img_i = 255-np_img #(255 is max pixel value for uint8 array)
#Binarise each colour channel
#Threshold = 99 #anything above 99 will be turned to 255 value
#np_img_boolean = np_img > Threshold #using a comparison operator on a ndarray creates a new array of boolean values
#np_img_bin = np.empty(np_img.shape)#create empty ndarray
#np_img_bin[:,:]= np_img_boolean * 255#iterate through the boolean array and multiply each element by 255.  True = 1 and False = 0 so only 'True' elements are multiplied
#trim the image, or crop a specific section
#np_img_trim = np_img[372:411,292:328,:]#ymin:ymax,xmin:xmax - bounding box from xml file. you can trim for just one colour channel too
#split the image horizontally down the middle
#np_img1, np_img_2 = np.hsplit(np_img,2)
#or split vertically - this time supply multiple y coordinates to split at
#np_img1, np_img_2, np_img3 = np.vsplit(np_img,[200,300])#200 and 300 represents the y axis as its vertical
#overlay one image onto another using slicing
#np_img_overlay = np_img.copy()
#np_img_overlay[100:200,:] = np_img_2#make sure the size of the area you are overlaying matches the size of np_img2
#print(np_img_overlay.shape)
#Blend two images together
#np_img_blend = np_img*0.5 + np_img2*0.5
#You can also add a base pixel value per colour channel during the blending
#np_img_blend = np_img*0.5 + np_img2*0.5 + (100,0,0)#Colour Channel is (R,G,B)
#np_img_blend = np_img_blend.clip(0,255)#use clip() to keep all pixel values within 255 needed for uint8
#convert back to PIL image. Note above calculation changes the dtype of ndarray into float so we need to convert it back to uint8
#new_img = Image.fromarray(np.uint8(np_img_blend))
#new_img.show()
#imhist, bins = np.histogram(np_img.flatten(),256,normed=True)

#If you have a particular range of values that you want to binarise for (e.g. a red ball) you can use the
#np.where and np.logical_and function like so:
#np_img_bin = np.empty([480,640,1])#create empty ndarray
#replace empty array value with 1 or 1.25 depending on pixel value matching logical_and condition
#np_img_bin[:,:,:] = np.where((np.logical_and(img[:,:,[0]] > 100,img[:,:,[1]] < 70,img[:,:,[2]] < 70)),1.25,1)
#this creates a 1d array which has 1.25 just for the pixels which are most 'red'
#multiply pixels on original image by 1 or 1.25 depending on the 1d array, but for red channel only. Need to apply max score of 255(clip)
#np_img_bins = np.clip((im[:,:,[0]] * np_img_bin),0,255)
#add values from original image to the green and blue channels
#for i in range(1,3):
#    np_img_bins = np.insert(np_img_bins,i,im[:,:,i],axis = 2)#inserts before indicies 1, value im[:,:,i], along axis 2

#Element-wise maths - performing a calculation on each element of the array in turn with one command
x = np.array([[1, 2], [3, 4]])
y = np.array([[5,6],[7,8]])
#print(x.sum())#adds all elements in an array
#print(x + y)#adds pairs of elements from both arrays
#print (x * y)#multiple pairs of elements from both arrays
#print(x.sum(axis=0) )  # columns (first dimension)
#print(x.sum(axis=1) )  # rows (second dimension)
#z = np.array([[1, 2, 3],[4,5,6]])
#print(z.min())#min across array
#print(z.max())#max across array
#print(z.argmin())  # index of minimum
#print(z.argmax())  # index of maximum
#Array-wise maths
#print(np.concatenate((x,y),axis = None))#flatten and add
#print(np.concatenate((x,y),axis = 0))#add by row
#print(np.concatenate((x,y),axis = 1))#add by column

#statistics calculations
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
#print(y.mean())#add all elements together and divide by number of elements
#print(np.median(y))#value in middle of lowest and highest element
#print(np.median(y, axis=-1)) # last axis
#print(x.std())#standard devition
#Sorting and Broadcasting
y.sort(axis=0)
#print(y)
a = np.array([4, 3, 1, 2])
j = np.argsort(a)#returns an array of the index numbers of (a), sorted by value from smallest to largest
#print(j)
#print(a[j])#returns the array of sorted values
#Broadcasting
#an array of distances (in miles) between cities of Route 66: Chicago, Springfield,
# Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff and Los Angeles.
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,
       1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])#each element in mileposts minus all of the other elements in turn
print(distance_array)
#use numpy iteration functions to loop through the multidimensional image ndarrays
#for i in np.nditer(mileposts):
#    print(i)
for counter, value in np.ndenumerate(distance_array):
    print(counter, value)



