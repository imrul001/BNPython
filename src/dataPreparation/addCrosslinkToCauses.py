#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "imrul"
__date__ = "$Jan 25, 2016 8:53:21 PM$"

import sys
import csv

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

datafile = sys.argv[1];
exactfile = sys.argv[2];

length=file_len(datafile);
nearest = range(length);
i=0;
with open(datafile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        nearest[i] = row[29];
        i=i+1;

with open(exactfile, 'rb') as csvfile1:
    reader1 = csv.reader(csvfile1, delimiter=',')
    index = 0;
    for row in reader1:
        if(index == 0):
            sys.stdout.write(row[0]+","+row[1]+","+row[2]+","+row[3] + ","+row[4] + "," + row[5]+ "," + nearest[index]+"\n");
            index = index + 1;
            count = 0;
        else:
            if(count < 100):
                sys.stdout.write(row[0]+","+row[1]+","+row[2]+","+row[3] + ","+row[4] + "," + row[5]+ "," + nearest[index]+"\n");
                count = count + 1;
            else:
                count = 0;
                index = index + 1;
