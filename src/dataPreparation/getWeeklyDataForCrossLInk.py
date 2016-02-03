#! /usr/bin/python

__author__ = "imrul"
__date__ = "$Jan 18, 2016 5:12:17 PM$"

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
#6. Rainfall_w0
#7. NDVI_w0
#8. lst_w0
#9. malaria_w0
#10. Month_w1
#11. Rainfall_w1
#12. NDVI_w1
#13. lst_w1
#14. malaria_w1
#15. Month_w2
#16. Rainfall_w2
#17. NDVI_w2
#18. lst_w2
#19. malaria_w2
#20. rainfall_wm1
#21. rainfall_wm2
#
#22. malaria_nearest_1st
#23. malaria_nearest_2nd
#24. malaria_nearest_3rd
#25. Sum_of_nesrest
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

def getIncidence(year, week, yearList, weekList, vidList, malaria_w0List, nearestList):
    incidence_w0 = list();
    incidence_w0 = ["*","*","*"];
    i = 0;
    for i in range(0,len(nearestList)):
        if(nearestList[i]!="*"):
            n=0;
            for n in range(0, len(malaria_w0List)):
                if(year == yearList[n] and week == weekList[n] and nearestList[i] == vidList[n]):
#                    incidence_w0.append(int(malaria_w0List[n]));
                    incidence_w0[i] = int(malaria_w0List[n]);
                    break;
        else:
#            incidence_w0.append("*")
            incidence_w0[i] = "*";
    return incidence_w0;

def getSum(nearestIncidences):
    i = 0;
    sum = 0;
    for i in range(len(nearestIncidences)):
        if(nearestIncidences[i] != "*"):
            sum = sum+int(nearestIncidences[i]);
    return sum;

length=file_len(dataFile);
yearList = range(length);
weekList = range(length);
malaria_w0List = range(length);
vidList = range(length);
i=0;
with open(dataFile, 'rb') as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',')
    for row in reader2:
        yearList[i] = row[0];
        weekList[i] = row[2];
        malaria_w0List[i] = row[16];
        vidList[i] = row[3];
        i=i+1;

index = 0;
with open(nearestFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with open(dataFile, 'rb') as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=',')
        for row in reader1:
            if(index == 0):
                n_1 = "nearest_1st";
                n_2 = "nearest_1st";
                n_3 = "nearest_1st";
                sum123 = "sum_123";
                sys.stdout.write(row[1] + "," + row[4] + "," + row[5] + "," + row[6] + "," + row[8] + "," +
                                 row[9] + "," + row[10] + "," + row[11] + "," + row[16] + "," + row[18] + "," +
                                 row[20] + "," + row[21] + "," + row[22] + "," + row[27] + "," + row[29] + "," +
                                 row[31] + "," + row[32] + "," + row[33] + "," + row[38] + "," + row[50] + "," +
                                 row[56] + "," + str(n_1) + "," + str(n_2) + "," + str(n_3) + "," + str(sum123) + "\n");
            else:
                village_id = row[3];
                year = row[0];
                week = row[2];
                csvfile.seek(0);
                nearestList = list();
                nearestList = getNearest(village_id, reader);
                nearestIncidences_w0 = list();
                nearestIncidences_w0 = getIncidence(year, week, yearList, weekList, vidList, malaria_w0List, nearestList);
                sum123 = getSum(nearestIncidences_w0);
                sys.stdout.write(row[1] + "," + row[4] + "," + row[5] + "," + row[6] + "," + row[8] + "," +
                                 row[9] + "," + row[10] + "," + row[11] + "," + row[16] + "," + row[18] + "," +
                                 row[20] + "," + row[21] + "," + row[22] + "," + row[27] + "," + row[29] + "," +
                                 row[31] + "," + row[32] + "," + row[33] + "," + row[38] + "," + row[50] + "," +
                                 row[56]+ "," + str(nearestIncidences_w0[0]) + "," + str(nearestIncidences_w0[1]) + "," + str(nearestIncidences_w0[2]) + "," + str(sum123) + "\n");
            index = index + 1;
sys.stdout.flush();



    
