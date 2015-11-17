#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 22, 2015 8:40:28 PM$"

import sys
import csv

probFile = sys.argv[1];

def getRowDynamically(row):
    total = "";
    num_cols = len(row);
    for i in range(0, num_cols):
	if(i == 0):
            total = row[i] + ",";
	if(i > 0 and i < (num_cols -1)):
            total = total + row[i] + ",";
        if(i == (num_cols -1)):
            total = total + row[i] + "\n";	
	return total;



with open(probFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(row[8] != str("0")):
#            sys.stdout.write(getRowDynamically(row));
            sys.stdout.write(row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+"\n");
        
            


