#!/usr/bin/python

__author__ = "imrul"
__date__ = "$Oct 20, 2015 11:37:03 PM$"

import csv
import random
import sys
import dataPreparation.random_sampling

# This method replaces the probabilities by a randomely choose value(incidence rates)
def getRandomlyChosenValue(eachEntry):
#    Split , from each entry
    r = eachEntry.split(","); 
#    get each probability of the cause in data list
    data = r[0].split(";");
    state = getRandomState(data);
    return str(getTheMidPoint(state));


# This method randomly choose actual incidence rate(0-1) 
# and return the state that the random number is in.
# Here data is a list of probabilities of each entry.
def getRandomState(data):
#    generate random number(0.0 <=  randNumber <=1.0)
    randNumber = random.random();
    state = 10;
    bound0 = float(data[0]);
    bound1 = bound0 + float(data[1]);
    bound2 = bound1 + float(data[2]);
    bound3 = bound2 + float(data[3]);
    bound4 = bound3 + float(data[4]);
#    bound5 = bound4 + float(data[5]);
    # sys.stdout.write("random number = "+str(randNumber)+"\n");
    # sys.stdout.write("bound0 "+str(bound0)+" bound1 "+str(bound1)+" bound2 "+str(bound2)+" bound3 "+str(bound3)+" bound4 "+str(bound4)+"\n");
    if(randNumber > 0 and randNumber <= bound0):
        state = 0;
    if(randNumber > bound0 and randNumber <= bound1):
        state = 1;
    if(randNumber > bound1 and randNumber <= bound2):
        state = 2;
    if(randNumber > bound2 and randNumber <= bound3):
        state = 3;
    if(randNumber > bound3 and randNumber <= bound4):
        state = 4;
#    if(randNumber > bound4 and randNumber <= bound5):
#        state = 5;
    return state;

# This method gets the midpoint by each state(0,1,2,3,4)
def getTheMidPoint(state):
    ranges = list();
    ranges_w1 = list();
    ranges_w2 = list();
    ranges_w3 = list();

    s2BinList = list()
    s2BinList = [2,3,4];
    s2FreqList = list();
    s2FreqList = [129, 92, 76];

    s3BinList = list();
    s3BinList = [6.6, 8.2, 9.8, 11.4, 13];
    s3FreqList = list();
    s3FreqList =[89, 66, 32, 29, 36];
    
    s4BinList = list();
    s4BinList = [49.375, 84.75, 120.125, 155.5, 190.875, 226.25, 297];
    s4FreqList = list();
    s4FreqList =[203, 30, 11, 4, 3, 2, 1];

    ranges_w1 = [0.0, 0.98, 1.5, 4.5, 13.5, 297];
    ranges_w2 = [0.0, 0.5, 1.5, 4.5, 13.5, 297];
    ranges_w3 = [0.0, 0.5, 1.5, 4.5, 13.5, 297];

    ranges = ranges_w1;
    midPoint = 0.0;
    
    randomExact = 0.0;
    if(state == 0):
        midPoint = calculateMidpoint(ranges[0], ranges[1]);
        midPoint = 0.0;
    if(state == 1):
        midPoint = calculateMidpoint(ranges[1], ranges[2]);
        midPoint = 1.0;
    if(state == 2):
        midPoint = calculateMidpoint(ranges[2], ranges[3]);
#        midPoint = dataPreparation.random_sampling.generateRandomPointbyDistribution(s2BinList, s2FreqList, 1.5);
        midPoint = 2.821549;
    if(state == 3):
        midPoint = calculateMidpoint(ranges[3], ranges[4]);
#        midPoint = dataPreparation.random_sampling.generateRandomPointbyDistribution(s3BinList, s3FreqList, 4.5);
        midPoint = 8.007;
    if(state == 4):
        midPoint = calculateMidpoint(ranges[4], ranges[5]);
#        midPoint = dataPreparation.random_sampling.generateRandomPointbyDistribution(s4BinList, s4FreqList, 13.5);
        midPoint = 38.42745;
    if(state == 5):
        midPoint = 58.77419;
    return midPoint;    


# This method calculates the mid point between two points
def calculateMidpoint(lowerBound, upperBound):
    return float((lowerBound + upperBound) / 2);
    #return float(random.uniform(lowerBound,upperBound))

#This method generates a random number between the given ranges
def generateUniformRandom(lowerbound, uppderBound):
    return float(random.uniform(lowerbound, uppderBound));

# This is the input csv(, delimited)file by command line.
dataFile = sys.argv[1];

# Main Body of the Program
numberOfSamples = 100;
id = 1;
with open(dataFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0;
    numberOfSamples = 0;
    for row in reader:
        randomN = 0;
        if(i == 0):
            sys.stdout.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + ","+"month,"+"id"+"\n");
        if(i != 0):
            if(float(row[5]) == 0.0):
                randomN = 100;
            if(float(row[5]) > 0.5 and float(row[5]) <= 1.5):
                randomN = 100;
            if(float(row[5]) > 1.5 and float(row[5]) <= 4.5):
                randomN = 100;
            if(float(row[5]) > 4.5 and float(row[5]) <= 13.5):
                randomN = 100;
            if(float(row[5]) > 13.5 and float(row[5]) <= 26.5):
                randomN = 100;
            if(float(row[5]) > 26.5):
                randomN = 100;
            j = 0;
            for j in range(0, randomN):
                sys.stdout.write(getRandomlyChosenValue(row[0]) + "," + getRandomlyChosenValue(row[1]) + ","
                                 + getRandomlyChosenValue(row[2]) + "," + getRandomlyChosenValue(row[3]) + ","
                                 + getRandomlyChosenValue(row[4]) + "," + row[5] + "\n");
                id = id +1;                 
        i = i + 1;    