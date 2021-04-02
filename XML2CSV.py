'''Convert a file of xml bounding box annotations into a csv file for
use with the google cloud AutoML vision module'''

import pandas as pd
import xmltodict
import os

xmlsource = "/Users/tobieabel/Desktop/BallXML_Test"
xmlFiles = sorted([i for i in os.listdir(xmlsource)if i != ".DS_Store"])
column_names = ['set', 'uri', 'label', 'xmin', 'ymin', 'xmax', 'ymax']#don't actually need the column names for AutoML, but kept here if you need to do same for other deep learning
csv_list = []

for i in xmlFiles:#iterate through files in folder - here just using one forlder for 'TRAIN' set, but can use other folders for VALIDATE and TEST sets
    with open(xmlsource + '/' + i,'r') as xml:
        data_dict = xmltodict.parse(xml.read())
        if type(data_dict['annotation']['object']) ==  list:#i.e multiple balls
            for x in (data_dict['annotation']['object']):#loop through the object dict
                label = x['name']
                set = 'TRAIN'#i manully changed some of these to VALIDATE and SET on csv file once its produced
                URI = 'gs://roboticsaiautoml/Ball_Test/'+ i[:-3] + 'jpg'#this is the name of the bucket where the images are.  Currently has to be in US region
                xmin = float(int(x['bndbox']['xmin'])/640)#converting the coordinates into floating point between 0 and 1
                ymin = float(int(x['bndbox']['ymin'])/480)
                xmax = float(int(x['bndbox']['xmax'])/640)
                ymax = float(int(x['bndbox']['ymax'])/480)
                line_list = [set,URI,label,xmin,ymin,'','',xmax,ymax,'','']#AutoML allows you to enter additional x and y values, but i don't need them so they are left blank
                csv_list.append(line_list)
                line_list = []
        else:#only one ball
            label = data_dict['annotation']['object']['name']
            set = 'TRAINING'
            URI = 'gs://roboticsaiautoml/Ball_Test/'+ i[:-3] + 'jpg'
            xmin = float(int(data_dict['annotation']['object']['bndbox']['xmin'])/640)
            ymin = float(int(data_dict['annotation']['object']['bndbox']['ymin'])/480)
            xmax = float(int(data_dict['annotation']['object']['bndbox']['xmax'])/640)
            ymax = float(int(data_dict['annotation']['object']['bndbox']['ymax'])/480)
            line_list = [set, URI, label, xmin, ymin,'','', xmax, ymax,'','']
            csv_list.append(line_list)
            line_list = []

xml_df = pd.DataFrame(csv_list)#don't need to add column headings for google AutoML
xml_df.to_csv(xmlsource + '/labels.csv')#create the csv file in the same folder as the xml files