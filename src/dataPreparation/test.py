#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 29, 2015 4:39:34 PM$"

import csv
import sys

fileName = sys.argv[1];
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count = 0;
    for row in reader:
        if(count != 0):
            if(float(row[18]) > 5.5 and float(row[18]) < 82.1):
                sys.stdout.write(row[18] + "\n");
        count = count + 1;


