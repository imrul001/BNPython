#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Dec 21, 2015 10:59:54 PM$"

import sys
import csv
import math

uniqVillage = sys.argv[1];
dist = sys.argv[2];
radius = sys.argv[3];

def getDistance(x1, y1, x2, y2):
    distance = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)));
    return float(distance);

def printNearest(village_id, nList):
    line = village_id;
    count = 0;
    for vid in nList:
        if(count == 0):
            line = line+","+vid;
        
        
with open(uniqVillage, 'rb') as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',')
    with open(dist, 'rb') as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',')
        for row in reader2:
            village_id = row[0];
            x1_cor = float(row[1]);
            y1_cor = float(row[2]);
            csvfile1.seek(0);
            count = 0;
            sys.stdout.write(village_id)
            for r in reader1:
                if(count > 0):
                    if(village_id != r[1]):
                        x2_cor = float(r[4]);
                        y2_cor = float(r[5]);
                        distance = getDistance(x1_cor, y1_cor, x2_cor, y2_cor);
                        if(distance < float(radius)):
                            sys.stdout.write(","+str(r[1]));
                count = count + 1;
            sys.stdout.write("\n");            
        

