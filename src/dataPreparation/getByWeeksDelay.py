#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 25, 2015 12:45:18 PM$"

import sys
import csv

fileName = sys.argv[1];
weekDelay = sys.argv[2];
villageId = sys.argv[3];

weeks2 = list();
weeks3 = list();
weeks4 = list();
years = list();
years = [2012,2013,2014];

iterationWeek = list();

weeks2 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,53]

weeks3 = [3,6,9,12,15,18,21,24,27,30,33,36,39,41,44,47,50,53]

weeks4= [4,8,12,16,20,24,28,32,36,40,44,48,52,53]


weekDelay = int(weekDelay);
if(weekDelay == 2):
    iterationWeek = weeks2;
if(weekDelay == 3):
    iterationWeek = weeks3;
if(weekDelay == 4):
    iterationWeek = weeks4;
s1 = weekDelay - 1;

count = 0;
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for year in years:
        for j in iterationWeek:
            start = j - s1;
            csvfile.seek(0);
            total = 0;
            for row in reader:
                if(count !=0):
                    if(row[0] == villageId and int(row[1])<=j and int(row[1])>=start and row[3]!="" and str(year)== row[30]):
                        if(row[14]==""):
                            row[14]="0";
                        if(row[15]==""):
                            row[15]="0";
                        total = total + int(row[14]) + int(row[15]);
                else:
                    sys.stdout.write("year,week,incidences\n");    
                count = count + 1;
            sys.stdout.write(str(year)+","+str(j)+","+str(total)+"\n");
            
        

