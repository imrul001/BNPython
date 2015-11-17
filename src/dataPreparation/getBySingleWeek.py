#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Nov 4, 2015 10:04:01 PM$"

import sys
import csv

fileName = sys.argv[1];
villageId = sys.argv[2];

years = list();
years = [2012, 2013, 2014];

count = 0;
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for year in years:
        csvfile.seek(0);
        total = 0;
        for row in reader:
            if(count != 0):
                if(row[0] == villageId and row[3] != "" and str(year) == row[30]):
                    if(row[14] == ""):
                        row[14] = "0";
                    if(row[15] == ""):
                        row[15] = "0";
                    total = int(row[14]) + int(row[15]);
                    sys.stdout.write(str(year) + "," + str(row[1]) + "," + str(total) + "\n");
            else:
                sys.stdout.write("year,week,incidences\n");    
            count = count + 1;
        