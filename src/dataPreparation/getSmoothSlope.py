#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Jan 31, 2016 7:44:50 PM$"

import sys
import csv

dataFile = sys.argv[1];

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getAverage(v1,v2,v3):
    sum=float(v1)+float(v2)+float(v3);
    return sum/3;

length=file_len(dataFile);
slope=range(length);

i=0;
with open(dataFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        slope[i]=row[22];
        i=i+1;

r = 0;
for r in range(0,len(slope)):
    if (r > 1 and r < len(slope)-1):
        smoothedSlope = getAverage(slope[r-1], slope[r], slope[r+1]);
        sys.stdout.write(str(smoothedSlope)+"\n");
