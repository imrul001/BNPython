#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 26, 2015 11:14:31 PM$"

import sys

sys.stdout.write("Script to generate Model data By weeks Interval\n");

####Output format

#*** week group means the given group of weeks
#Month_w0=Month_of_week_group
#Year==Year_Week_group
#Village_id == Village_Id

#Dist_to_stream= distance from the village to the stream
#Dist_to_border= distance from the village to the border
#stream_density = Stream density of the village
#slope = slope of the village

#rainfall_w0 = rainfall of week_group
#NDVI_w0 = NDVI of the week_group
#LST_w0 = LST of the week group

#Malaria_w0 == Malaria Incidences of week_group

#Month_w1=Month_of_week_group+1
#Year==Year_Week_group+1
#rainfall_w0 = rainfall of week_group+1
#NDVI_w0 = NDVI of the week_group+1
#LST_w0 = LST of the week group+1
#Malaria_w1 == Malaria Incidences of week_group+1

#Month_w1=Month_of_week_group+2
#Year==Year_Week_group+2
#rainfall_w0 = rainfall of week_group+2
#NDVI_w0 = NDVI of the week_group+2
#LST_w0 = LST of the week group+2
#Malaria_w1 == Malaria Incidences of week_group+2

#Month_w1=Month_of_week_group+3
#Year==Year_Week_group+3
#rainfall_w0 = rainfall of week_group+3
#NDVI_w0 = NDVI of the week_group+3
#LST_w0 = LST of the week group+3
#Malaria_w1 == Malaria Incidences of week_group+3

### Required File and input
# unique_village_Id_file
# Malaria case file
# Rainfall file
# LST file
# NDVI file
# week_group

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1;

unique_village_file = sys.argv[1];
week_group = sys.argv[2]
current_model_file = sys.argv[3];

length=file_len(unique_village_file);
vid=range(length);
i=0;
with open(unique_village_file, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        vid[i]=row[0];
        i=i+1;

years = list();
years = [2012,2013,2014];
iterationWeek = list();
weeks2 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54]
weeks3 = [3,6,9,12,15,18,21,24,27,30,33,36,39,41,44,47,50,53]
weeks4= [4,8,12,16,20,24,28,32,36,40,44,48,52,54]
weekDelay = int(weekDelay);
if(weekDelay == 2):
    iterationWeek = weeks2;
if(weekDelay == 3):
    iterationWeek = weeks3;
if(weekDelay == 4):
    iterationWeek = weeks4;
s1 = weekDelay - 1;



