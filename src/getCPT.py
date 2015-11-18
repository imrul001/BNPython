#! /usr/bin/python
__author__ = "imrul"
__date__ = "$Oct 20, 2015 11:43:32 PM$"

import csv
import math
import sys
import dataPreparation.random_sampling

# =EXP($J$8+(A2*$J$9)+(B2*$J$10)+(C2*$J$11)+(D2$J$12)+(E5*$J$13))

def getFuntionValueForPoisson(SLOPE_RAINFALL, DIST_TO_BORDER, NDVI, DIST_TO_STREAM, STREAM_DENSITY, week):
    eff_1 = list();
    eff_2 = list();
    eff_3 = list();
    eff = list();
    
    eff_1 = [-1.0322622, 0.0960439,0.0441000,0.1037926,0.1056194,0.1093415];
    eff_2 = [-2.860191, 0.235727, 0.098182, 0.217419, 0.255139, 0.252388];
    eff_3 = [-2.846142, 0.237893, 0.098829, 0.222521, 0.258851, 0.247076];
    if(week == "1"):
        eff = eff_1;
    if(week == "2"):
        eff = eff_2;
    if(week == "3"):
        eff = eff_3;	
    result = eff[0] + (SLOPE_RAINFALL * eff[1]) + (DIST_TO_BORDER * eff[2]) + (NDVI * eff[3]) + (DIST_TO_STREAM * eff[4]) + (STREAM_DENSITY * eff[5]);
    return math.exp(result);
    # return result;


def getMidPoint(state, week):
    ranges = list();
    ranges_w1 = list();
    ranges_w2 = list();
    ranges_w3 = list();

    # 0.0057,0.073,0.19534225,0.3918015,3.634336

    ranges_w1 = [0.0, 0.5, 1.5, 2.5, 5.5, 82];
    ranges_w2 = [0.0, 0.5, 1.5, 2.5, 5.5, 82];
    ranges_w3 = [0.0, 0.5, 1.5, 2.5, 5.5, 82];

    if(week == "1"):
        ranges = ranges_w1;	
    if(week == "2"):
        ranges = ranges_w2;	
    if(week == "3"):
        ranges = ranges_w3;		
    midPoint = 0.0;

    if(state == "s0"):
        midPoint = calculateMidpoint(ranges[0], ranges[1]);
        midPoint = 0;
    if(state == "s1"):
        midPoint = calculateMidpoint(ranges[1], ranges[2]);
        midPoint = 1;
    if(state == "s2"):
        midPoint = calculateMidpoint(ranges[2], ranges[3]);
        midPoint = 2;
    if(state == "s3"):
        midPoint = calculateMidpoint(ranges[3], ranges[4]);
        midPoint = 4;
    if(state == "s4"):
        midPoint = calculateMidpoint(ranges[4], ranges[5]);
        midPoint = dataPreparation.random_sampling.generateRandomPointbyDistribution();
    return str(midPoint);

# This method calculates the mid point between two points
def calculateMidpoint(lowerBound, upperBound):
    return float((lowerBound + upperBound) / 2);

def getState(value, week):
    ranges = list();
    ranges_w1 = list();
    ranges_w2 = list();
    ranges_w3 = list();

    ranges_w1 = [0.0, 0.5, 1.5, 2.5, 5.5, 82];
    ranges_w2 = [0.0, 0.5, 1.5, 2.5, 5.5, 82];
    ranges_w3 = [0.0, 0.5, 1.5, 2.5, 5.5, 82];

#    sys.stdout.write("value =="+str(value)+",");

    if(week == "1"):
        ranges = ranges_w1;	
    if(week == "2"):
        ranges = ranges_w2;	
    if(week == "3"):
        ranges = ranges_w3;		

    value = float(value);
#    sys.stdout.write(str(value)+" value==");
    if(value > ranges[0] and value <= ranges[1]):
        return "s0";
    if(value > ranges[1] and value <= ranges[2]):
        return "s1";
    if(value > ranges[2] and value <= ranges[3]):
        return "s2";
    if(value > ranges[3] and value <= ranges[4]):
        return "s3";
    if(value > ranges[4]):
        return "s4";

def getProbabilities(eachCombinition, week):
    states = eachCombinition.split(",");
    SLOPE_RAINFALL = float(getMidPoint(states[0], week));
    DIST_TO_BORDER = float(getMidPoint(states[1], week));
    NDVI = float(getMidPoint(states[2], week));
    DIST_TO_STREAM = float(getMidPoint(states[3], week));
    STREAM_DENSITY = float(getMidPoint(states[4], week));
    result = getFuntionValueForPoisson(SLOPE_RAINFALL, DIST_TO_BORDER, NDVI, DIST_TO_STREAM, STREAM_DENSITY, week);
    return str(result);


def printEachEntry(resultProbability, week):
    state = getState(resultProbability, week);
    if(state == "s0"):
        return "1, 0, 0, 0, 0"
    if(state == "s1"):
        return "0, 1, 0, 0, 0"
    if(state == "s2"):
        return "0, 0, 1, 0, 0"
    if(state == "s3"):
        return "0, 0, 0, 1, 0"
    if(state == "s4"):
        return "0, 0, 0, 0, 1"

#state combination file
comboFile = sys.argv[1];
week = sys.argv[2];

with open(comboFile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        sys.stdout.write(printEachEntry(getProbabilities(row[0], week), week) + "\n");
