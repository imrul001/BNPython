#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "imrul"
__date__ = "$Jan 25, 2016 8:53:21 PM$"

import csv
import sys

dataFile = sys.argv[1];

with open(dataFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count = 0;
    for row in reader:
        if(count == 0):
            sys.stdout.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," +
                             row[5] + "," + row[6] + "," + row[7] + "," + row[8] + "," + row[9] + "," +
                             row[10] + "," + row[11] + "," + row[12] + "," + row[13] + "," + row[14] + "," +
                             row[15] + "," + row[16] + "," + row[17] + "," + row[18] + "," + row[19] + "," + row[20] + "," + row[21] + "," + "incidence_slope" + "\n");

        else:
            incidence_slope = str(float(row[22])+float(row[23]));
            sys.stdout.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," +
                             row[5] + "," + row[6] + "," + row[7] + "," + row[8] + "," + row[9] + "," +
                             row[10] + "," + row[11] + "," + row[12] + "," + row[13] + "," + row[14] + "," +
                             row[15] + "," + row[16] + "," + row[17] + "," + row[18] + "," + row[19] + "," + row[20] + "," + row[21] +","+incidence_slope+"\n");

        count = count + 1;
