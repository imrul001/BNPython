#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Jan 19, 2016 9:46:50 PM$"

import csv
import sys

#needed files
#1. Ep3 Weekly Data File with all info
#2. nearest village file

#output file
#1. Month_w0
#2. stream_dist
#3. border_dis
#4. slope
#5. stream denisty
#6. Rainfall_m0
#7. NDVI_m0
#8. lst_m0
#9. malaria_m0
#10. Month_m1
#11. Rainfall_m1
#12. NDVI_m1
#13. lst_w1
#14. malaria_m1
#15. Month_m2
#16. Rainfall_m2
#17. NDVI_m2
#18. lst_m2
#19. malaria_m2
#
#20. malaria_nearest_1st
#21. malaria_nearest_2nd
#22. malaria_nearest_3rd
#23. Sum_of_nesrest
#sys.stdout.write("Generates Cross Link Data\n");


dataFile = sys.argv[1];
nearestFile = sys.argv[2];

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getNearest(village_id, reader):
    nearest = list();
    for row in reader:
        if(row[0] == village_id and len(row) == 2):
            nearest.append(row[1]);
            nearest.append("*");
            nearest.append("*");
            break;
        if(row[0] == village_id and len(row) == 3):
            nearest.append(row[1]);
            nearest.append(row[2]);
            nearest.append("*");
            break;
        if(row[0] == village_id and len(row) == 4):
            nearest.append(row[1]);
            nearest.append(row[2]);
            nearest.append(row[3]);
            break;
    if(len(nearest) < 1):
        nearest.append("*");
        nearest.append("*");
        nearest.append("*");
    return nearest;

def getIncidence(year, month, yearList, monthList, vidList, malaria_m0List, nearestList):
    incidence_m0 = list();
    incidence_m0 = ["*","*","*"];
    i = 0;
    for i in range(0,len(nearestList)):
        if(nearestList[i]!="*"):
            n=0;
            for n in range(0, len(malaria_m0List)):
                if(year == yearList[n] and month == monthList[n] and nearestList[i] == vidList[n]):
#                    incidence_w0.append(int(malaria_w0List[n]));
                    incidence_m0[i] = int(malaria_m0List[n]);
                    break;
        else:
#            incidence_w0.append("*")
            incidence_m0[i] = "*";
    return incidence_m0;

def getSum(nearestIncidences):
    i = 0;
    sum = 0;
    for i in range(len(nearestIncidences)):
        if(nearestIncidences[i] != "*"):
            sum = sum+int(nearestIncidences[i]);
    return sum;

length=file_len(dataFile);
yearList = range(length);
monthList = range(length);
malaria_m0List = range(length);
vidList = range(length);
i=0;
with open(dataFile, 'rb') as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',')
    for row in reader2:
        yearList[i] = row[16];
        monthList[i] = row[17];
        malaria_m0List[i] = row[25];
        vidList[i] = row[2];
        i=i+1;


index = 0;
with open(nearestFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with open(dataFile, 'rb') as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',')
        for row in reader1:
            if(index == 0):
                n_1 = "nearest_1st";
                n_2 = "nearest_2nd";
                n_3 = "nearest_3rd";
                sum123 = "sum_123";
                sys.stdout.write(row[1] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[7] + "," +
                                 row[8] + "," + row[9] + "," + row[14] + "," + row[15] + "," + row[17] + "," +
                                 row[18] + "," + row[19] + "," + row[20] + "," + row[25] + "," + row[27] + "," +
                                 row[28] + "," + row[29] + "," + row[30] + "," + row[35] +"," +
                                 str(n_1) + "," + str(n_2) + "," + str(n_3) + "," + str(sum123) + "\n");
            else:
                village_id = row[2];
                year = row[0];
                month = row[1];
                csvfile.seek(0);
                nearestList = list();
                nearestList = getNearest(village_id, reader);
                nearestIncidences_m0 = list();
                nearestIncidences_m0 = getIncidence(year, month, yearList, monthList, vidList, malaria_m0List, nearestList);
                sum123 = getSum(nearestIncidences_m0);
                sys.stdout.write(row[1] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[7] + "," +
                                 row[8] + "," + row[9] + "," + row[14] + "," + row[15] + "," + row[17] + "," +
                                 row[18] + "," + row[19] + "," + row[20] + "," + row[25] + "," + row[27] + "," +
                                 row[28] + "," + row[29] + "," + row[30] + "," + row[35]+ "," +
                                 str(nearestIncidences_m0[0]) + "," + str(nearestIncidences_m0[1]) + "," + str(nearestIncidences_m0[2]) + "," + str(sum123) + "\n");
            index = index + 1;
sys.stdout.flush();