#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Nov 9, 2015 9:52:46 PM$"

import sys
import csv


ndviFile = sys.argv[1]

with open(ndviFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count = 0;
    for row in reader:
        if(count !=0):
            i = 1;
            index = 5;
            for i in range(1,13):
                sys.stdout.write(row[1]+","+str(i)+","+row[index]+"\n");
                index = index + 1;
        else:
            sys.stdout.write("VillageID,Month,NDVI\n");
        count = count + 1;


