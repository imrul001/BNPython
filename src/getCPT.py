#! /usr/bin/python
__author__ = "imrul"
__date__ = "$Oct 20, 2015 11:43:32 PM$"

import csv
import math
import sys
import dataPreparation.random_sampling

# =EXP($J$8+(A2*$J$9)+(B2*$J$10)+(C2*$J$11)+(D2$J$12)+(E5*$J$13))

def getCPTEntry(state, numberOFstate):
    index = 0;
    cptEntry = "";
    numberOFstate = int(numberOFstate);
    for index in range(0,numberOFstate):
        if(state == "s"+str(index)):
            for i in range(0, numberOFstate):
                if(index == i):
                    add = "1";
                else:
                    add = "0";
                if(i == 0):
                    cptEntry = add;
                else:
                    cptEntry = cptEntry + ", "+add;
            break;
    return cptEntry;

def getStateFromRange(value, ranges):
    state = "";
    index = 0;  
    value = float(value);
    if(float(value) < 0):
        value = 0.0
    for index in range(0, len(ranges)):
        if(index != len(ranges)-1):
            if(value >= float(ranges[index]) and value < float(ranges[index+1])):
                state = "s"+str(index);
                break;
        else:
            if(value >= float(ranges[index])):
                state = "s"+str(index-1);
                break;
    return state;

def getFuntionValueForPoisson(SLOPE_RAINFALL, DIST_TO_BORDER, NDVI, DIST_TO_STREAM, STREAM_DENSITY, nearest_sum, week):
    eff_1 = list();
    eff_2 = list();
    eff_3 = list();
    eff = list();
#    Hurdle model    
#    eff_1 = [-0.1447601, 0.0325562, 0.0273678, 0.0371324, 0.0343353, 0.0411477];

    eff_1 = [0.3267298, 0.0263652, 0.0365595, 0.0047537, 0.0038788, 0.0051445];
    eff_2 = [-2.860191, 0.235727, 0.098182, 0.217419, -0.0341719, 0.252388];
    eff_3 = [-2.846142, 0.237893, 0.098829, 0.222521, 0.258851, 0.247076];
    
    eff_1 = [0.1730879, 0.0221619, 0.0319645, 0.0041213, 0.0031739, 0.0038853, 0.0484235];
    if(week == "1"):
        eff = eff_1;
    if(week == "2"):
        eff = eff_2;
    if(week == "3"):
        eff = eff_3;    
    result = eff[0] + (SLOPE_RAINFALL * eff[1]) + (DIST_TO_BORDER * eff[2]) + (NDVI * eff[3]) + (DIST_TO_STREAM * eff[4]) + (STREAM_DENSITY * eff[5]) +(nearest_sum * eff[6]);
    # sys.stdout.write(str(math.exp(result))+",");
    return math.exp(result);
#    sys.stdout.write(str(result)+",");
#    return result;


def getMidPoint(state, week):
    ranges = list();
    ranges_w1 = list();
    ranges_w2 = list();
    ranges_w3 = list();

    # 0.0057,0.073,0.19534225,0.3918015,3.634336

#    ranges_w1 = [0.0, 0.98, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 9.5, 11.5, 13.5, 15.5, 18.5, 25.5, 30.5, 297];
#    ranges_w2 = [0.0, 0.5, 1.5, 2.5, 5.5, 6.5, 8.5, 11.5, 16.5, 19.5, 25.5, 34, 82];
#    ranges_w3 = [0.0, 0.5, 1.5, 2.5, 5.5, 6.5, 8.5, 11.5, 16.5, 19.5, 25.5, 34, 82];


    if(week == "1"):
        ranges = ranges_w1; 
    if(week == "2"):
        ranges = ranges_w2; 
    if(week == "3"):
        ranges = ranges_w3;     
    midPoint = 0.0;

    if(state == "s0"):
        # midPoint = calculateMidpoint(ranges[0], ranges[1]);
        midPoint = 0;
    if(state == "s1"):
        # midPoint = calculateMidpoint(ranges[1], ranges[2]);
        midPoint = 1;
    if(state == "s2"):
        # midPoint = calculateMidpoint(ranges[2], ranges[3]);
        midPoint = 2.821549;
    if(state == "s3"):
        # midPoint = calculateMidpoint(ranges[3], ranges[4]);
        midPoint = 8.007;
    if(state == "s4"):
        # midPoint = calculateMidpoint(ranges[4], ranges[5]);
        # midPoint = 6.4306;
        midPoint = 38.42745;
    return str(midPoint);

# This method calculates the mid point between two points
def calculateMidpoint(lowerBound, upperBound):
    return float((lowerBound + upperBound) / 2);

def getState(value, week):
    ranges = list();
    ranges_w1 = list();
    ranges_w2 = list();
    ranges_w3 = list();
    ranges_w1 = [0.0, 0.98, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5, 13.5, 15.5, 18.5, 25.5, 30.5, 297.1];
    ranges_w2 = [0.0, 0.5, 1.5, 2.5, 5.5, 6.5, 8.5, 11.5, 16.5, 19.5, 25.5, 34, 82];
    ranges_w3 = [0.0, 0.5, 1.5, 2.5, 5.5, 6.5, 8.5, 11.5, 16.5, 19.5, 25.5, 34, 82];

#    sys.stdout.write("value =="+str(value)+",");

    if(week == "1"):
        ranges = ranges_w1; 
    if(week == "2"):
        ranges = ranges_w2; 
    if(week == "3"):
        ranges = ranges_w3;     

    value = float(value);
#    sys.stdout.write(str(value)+" value==");
    return getStateFromRange(value, ranges);


def getProbabilities(eachCombinition, week):
    states = eachCombinition.split(",");
    SLOPE_RAINFALL = float(getMidPoint(states[0], week));
    DIST_TO_BORDER = float(getMidPoint(states[1], week));
    NDVI = float(getMidPoint(states[2], week));
    DIST_TO_STREAM = float(getMidPoint(states[3], week));
    STREAM_DENSITY = float(getMidPoint(states[4], week));
    nearest_sum = float(getMidPoint(states[5], week));
    result = getFuntionValueForPoisson(SLOPE_RAINFALL, DIST_TO_BORDER, NDVI, DIST_TO_STREAM, STREAM_DENSITY, nearest_sum, week);
    return str(result);


def printEachEntry(resultProbability, week):
    state = getState(resultProbability, week);
    return getCPTEntry(state, 17);


#state combination file
comboFile = sys.argv[1];
week = sys.argv[2];

with open(comboFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        sys.stdout.write(printEachEntry(getProbabilities(row[0], week), week) + "\n");


