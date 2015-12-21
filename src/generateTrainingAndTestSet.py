#!/usr/bin/python
# Author : Hasan
import csv
import re
import sys


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getFeatureList(argv, length):
  features = list();
  for n in range(3, length):
    features.append(int(sys.argv[n]));
  return features;

def getRowDynamically(row):
  total = "";
  num_cols = len(row);
  for i in range(0,num_cols):
    if(i == 0):
      total = row[i]+",";
    if(i > 0 and i < (num_cols -1)):
      total = total +row[i]+",";
    if(i == (num_cols -1)):
      total = total +row[i]+"\n"; 
  return total;

def generateTestData(reader, iterationNo, splitSize, fileLength, isLast, features):
  start = 0; end = 0;count = 0;
  if(isLast == 1):
    start = splitSize * (iterationNo - 1) + 1; 
    end = fileLength;
  else:
    start = splitSize * (iterationNo - 1) + 1;
    end = start + splitSize -1;
  fileOpen = open("Test-"+str(iterationNo)+".csv","wb");
  # print "Test";
  # sys.stdout.write(str(start)+" "+str(end)+" "+str(fileLength)+" "+str(splitSize)+"\n");
  for row in reader:
    if(count==0):
      fileOpen.write(getRowDynamically(row));
    if(start<=count):
      for i in range(0,len(features)):
        row[features[i]] = "*";
      fileOpen.write(getRowDynamically(row));
    if(end==count):
      break;
    count = count+1;
  fileOpen.close();

def generateTrainingSet(reader, iterationNo, splitSize, fileLength, isLast):
  start = 0; end = 0;count = 0;
  if(isLast == 1):
    start = splitSize * (iterationNo - 1) + 1; 
    end = fileLength;
  else:
    start = splitSize * (iterationNo - 1) + 1;
    end = start + splitSize -1;
  fileOpen = open("Train-"+str(iterationNo)+".csv","wb");
  # print "Train";
  # sys.stdout.write(str(start)+" "+str(end)+" "+str(fileLength)+" "+str(splitSize)+"\n");
  for row in reader:
    if(count==0):
      fileOpen.write(getRowDynamically(row));
    if((count < start and count!=0) or (count > end)):
      fileOpen.write(getRowDynamically(row));
    if(count==fileLength):
      break;
    count = count+1;
  fileOpen.close();



length = len(sys.argv);
fileName = "";
if(length < 3):
  sys.stdout.write("Incorrect Argument\n");
else:
  # This is the fold number
  k = int(sys.argv[1]); 
  fileName = sys.argv[2];
  fileLength = file_len(fileName.strip())-1;
  eachSplitSize = float(fileLength)
  features = list();
  features = getFeatureList(sys.argv, length);
  hasExtra = 0;
  isLast = 0;
  if(fileLength % k == 0):
    eachSplitSize = fileLength/k;
  else:
    hasExtra = 1;
    eachSplitSize = fileLength/k;

  for n in range(0,k):
    if(n == (k-1) and hasExtra == 1):
      isLast = 1;
    with open(fileName, 'rb') as csvfile2:  
      reader1 = csv.reader(csvfile2, delimiter=',')
      generateTrainingSet(reader1, n+1, eachSplitSize, fileLength, isLast);
    with open(fileName, 'rb') as csvfile1:
      reader = csv.reader(csvfile1, delimiter=',')
      generateTestData(reader, n+1, eachSplitSize, fileLength, isLast, features);
    
  # print length;
  # sys.stdout.write("each split : ");
  # print eachSplitSize;
  # sys.stdout.write("has extra : ");
  # print hasExtra;

sys.stdout.flush();