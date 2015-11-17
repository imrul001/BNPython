#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 23, 2015 5:57:13 PM$"

import csv
import math
import sys

fileName = sys.argv[1];
year = sys.argv[2];
#villageList = sys.argv[3];
#villageID = sys.argv[3];

weekNos = list();

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getMonth(weekNo):
    weekNo = int(weekNo);   
    month = 0;
#    count = 0;
#    li = list();
#    li = [1,5,6,9,10,13,14,18,19,22,23,26,27,31,32,35,36,39,40,44,45,48,49,52];
#    i = 0;  
#    for i in range(0,24):
#        if(weekNo >= li[i] and weekNo <= li[i+1]):
#            month = count;
#        else:
#            count=count+1;
            
    if(weekNo >= 1 and weekNo <= 5):
        month = 1;        
    if(weekNo >= 6 and weekNo <= 9):
        month = 2;        
    if(weekNo >= 10 and weekNo <= 13):
        month = 3;        
    if(weekNo >= 14 and weekNo <= 18):
        month = 4;        
    if(weekNo >= 19 and weekNo <= 22):
        month = 5;
    if(weekNo >= 23 and weekNo <= 26):
        month = 6;
    if(weekNo >= 27 and weekNo <= 31):
        month = 7;
    if(weekNo >= 32 and weekNo <= 35):
        month = 8;
    if(weekNo >= 36 and weekNo <= 39):
        month = 9;
    if(weekNo >= 40 and weekNo <= 44):
        month = 10;
    if(weekNo >= 45 and weekNo <= 48):
        month = 11;
    if(weekNo >= 49 and weekNo <= 52):
        month = 12;
    return month;

length = 2;
#length=file_len(villageList);
#vid=range(length);
#i = 0;
#with open(villageList, 'rb') as csvfile:
#    reader = csv.reader(csvfile, delimiter='\t')
#    for row in reader:
#        vid[i]=row[0];
#        i=i+1;

monthName = list();
monthName = ["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"];

index = 0; 
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count = 0;
    week53 = 0;
    k = 0;
    for k in range(0,length):
        villageId = "63050201";
        for month in range(1, 13):
            csvfile.seek(0);
            totalPositive = 0;
            for row in reader:
                if(count != 0):
                    if(year == row[30] and month == getMonth(int(row[1])) and villageId == row[9]):
                        if(row[14]==""):
                            row[14] = "0";
                        if(row[15]==""):
                            row[15] = "0";
                        totalPositive = totalPositive + int(row[14]) + int(row[15]);
                        index = index + 1;
                    if(year == row[30] and int(row[1]) > 52 and villageId == row[9]):
                        if(row[14] == ""):
                            row[14] = "0";
                        if(row[15] == ""):
                            row[15] = "0";
                        week53 = week53 + int(row[14]) + int(row[15]);
                else:
                    sys.stdout.write("Year,VillageID,Month,Total Positive\n");
                count = count + 1;
            if(totalPositive!=0):
                sys.stdout.write(year + "," +villageId +","+ str(month) + "," + str(totalPositive) + "\n");
        break;
sys.stdout.write(str(week53));





#sys.stdout.write(str(getMonth("47")) + "\n");
# 2012
#if(weekNo >= 1 and weekNo <= 5):
#        month = 1;        
#    if(weekNo >= 6 and weekNo <= 9):
#        month = 2;        
#    if(weekNo >= 10 and weekNo <= 13):
#        month = 3;        
#    if(weekNo >= 14 and weekNo <= 18):
#        month = 4;        
#    if(weekNo >= 19 and weekNo <= 22):
#        month = 5;
#    if(weekNo >= 23 and weekNo <= 26):
#        month = 6;
#    if(weekNo >= 27 and weekNo <= 31):
#        month = 7;
#    if(weekNo >= 32 and weekNo <= 35):
#        month = 8;
#    if(weekNo >= 36 and weekNo <= 39):
#        month = 9;
#    if(weekNo >= 40 and weekNo <= 44):
#        month = 10;
#    if(weekNo >= 45 and weekNo <= 48):
#        month = 11;
#    if(weekNo >= 49 and weekNo <= 52):
#        month = 12;
#    return month;

#2013
#    if(weekNo >= 2 and weekNo <= 5):
#        month = 1;        
#    if(weekNo >= 6 and weekNo <= 9):
#        month = 2;        
#    if(weekNo >= 10 and weekNo <= 13):
#        month = 3;        
#    if(weekNo >= 14 and weekNo <= 18):
#        month = 4;        
#    if(weekNo >= 19 and weekNo <= 22):
#        month = 5;
#    if(weekNo >= 23 and weekNo <= 26):
#        month = 6;
#    if(weekNo >= 27 and weekNo <= 31):
#        month = 7;
#    if(weekNo >= 32 and weekNo <= 35):
#        month = 8;
#    if(weekNo >= 36 and weekNo <= 40):
#        month = 9;
#    if(weekNo >= 41 and weekNo <= 44):
#        month = 10;
#    if(weekNo >= 45 and weekNo <= 48):
#        month = 11;
#    if(weekNo >= 49 and weekNo <= 52):
#        month = 12;
#    return month;

#2014
#if(weekNo >= 2 and weekNo <= 5):
#        month = 1;        
#    if(weekNo >= 6 and weekNo <= 9):
#        month = 2;        
#    if(weekNo >= 10 and weekNo <= 14):
#        month = 3;        
#    if(weekNo >= 15 and weekNo <= 18):
#        month = 4;        
#    if(weekNo >= 19 and weekNo <= 22):
#        month = 5;
#    if(weekNo >= 23 and weekNo <= 27):
#        month = 6;
#    if(weekNo >= 28 and weekNo <= 31):
#        month = 7;
#    if(weekNo >= 32 and weekNo <= 35):
#        month = 8;
#    if(weekNo >= 36 and weekNo <= 40):
#        month = 9;
#    if(weekNo >= 41 and weekNo <= 44):
#        month = 10;
#    if(weekNo >= 45 and weekNo <= 48):
#        month = 11;
#    if(weekNo >= 49 and weekNo <= 52):
#        month = 12;
#    return month;