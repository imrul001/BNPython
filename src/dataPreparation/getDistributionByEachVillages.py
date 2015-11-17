#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 24, 2015 11:04:53 AM$"

import sys
import csv


fileName = sys.argv[1];
village_id = sys.argv[2];

years = list();
years = [2012,2013,2014];
shortcut = [12,13,14];


#output format year week incidence number
count = 0;
index = 0;
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for year in years:
        csvfile.seek(0);
        for row in reader:
            if(count !=0):
                if(row[0] == village_id and row[30] == str(year)):
                    if(row[3]==""):
                        row[3]="0";
                    sys.stdout.write(str(year)+","+row[1]+","+row[3]+"\n");
            else:
                sys.stdout.write("year,week,incidences\n");
            count = count+1;
            sys.stdout.flush();
        index = index + 1;