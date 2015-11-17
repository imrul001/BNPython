#! /usr/bin/python

import csv
import sys


keys = sys.argv[1];
modelFile = sys.argv[2];

with open(keys, 'rb') as csvfile:
    reader1 = csv.reader(csvfile, delimiter=',')
    for row1 in reader1:
        year = row1[0];
        month = row1[1];
        vid = row1[2];
#        sys.stdout.write(year+","+month+","+vid+"\n");
        with open(modelFile, 'rb') as csvfile:
            reader2 = csv.reader(csvfile, delimiter=',')
            i = 0;
            for row2 in reader2:
                if(i!=0):
                    rainfall = 0.0;
                    if(year == row2[0] and int(row2[1]) == int(month)-1 and vid == row2[2]):
                        rainfall = float(row2[8]);
                        break;
                i=i+1;
            sys.stdout.write(str(rainfall) + "\n");

        





 


            