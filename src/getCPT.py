#! /usr/bin/python
__author__ = "imrul"
__date__ = "$Oct 20, 2015 11:43:32 PM$"

import csv
import math
import sys

# =EXP($J$8+(A2*$J$9)+(B2*$J$10)+(C2*$J$11)+(D2$J$12)+(E5*$J$13))

def getFuntionValueForPoisson(SLOPE_RAINFALL, DIST_TO_BORDER, NDVI, DIST_TO_STREAM, STREAM_DENSITY, week):
    eff_1 = list();
    eff_2 = list();
    eff_3 = list();
    eff = list();
    
#    poisson==eff_1 = [-0.2524, 0.01549, 0.005536, 0.01435, 0.01706, 0.01890];
#    zip_mid_0 ===eff_1 = [1.7498401, -0.4492147, -0.0158125, -0.0402851, -0.0351649, -0.0374318]
#    zip_mid === eff_1 = [2.2208451, -0.3733766, -0.0146031, -0.3115813, -0.024388, -0.3103967]
#   zip_random
#    eff_1 = [1.7727745, -0.0320003, -0.0129864, -0.3899677, -0.0326399, -0.0341625]
#   Linear Regression
#    eff_1 = [0.1737925, 0.0894477, 0.0160657, 0.0850058, 0.0978522, 0.1099574];
#mid point with poisson

#    eff_1 = [-2.671e-01, 1.524e-02, 5.545e-03, 1.479e-02, 1.713e-02, 1.881e-02];

#R-sq=0.3002
#    eff_1= [-0.0052270,0.0543379,0.0249545,0.0583767,0.0674259,0.0597816];
#R-sq=0.306
#   eff_1= [-0.4192962, 0.0527414, 0.0239367, 0.0591356, 0.0638277, 0.0600086];
# 30.2
#    eff_1= [-0.4167871, 0.0485557, 0.0225062, 0.0600918, 0.0650431,0.0589140];
#29.
#    eff_1= [0.2203034, 0.0520898, 0.0251213, 0.0582767, 0.0703513,0.0603191];
#best==    eff_1= [-0.0178389, 0.0503834, 0.0260136, 0.0579199, 0.0695520,0.0618606];
#best1== eff_1= [-0.0030582, 0.0456810, 0.0217269, 0.0553920, 0.0622497,0.0566454];
#best2===  eff_1= [-0.0314248, 0.0470156,0.0206798,0.0545907,0.0628409,0.0551295];
#new-b    eff_1= [0.0142586,0.0393981,0.0272951,0.0658727,0.0725503,0.0575656];
#eff_1= [-0.0505472,0.0376472,0.0251785,0.0588029,0.0694982,0.0554280];

    eff_1 = [-0.8582113, 0.0297849,0.0180236,0.0341691,0.0345780,0.0347838];
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
    if(state == "s1"):
        midPoint = calculateMidpoint(ranges[1], ranges[2]);
    if(state == "s2"):
        midPoint = calculateMidpoint(ranges[2], ranges[3]);
    if(state == "s3"):
        midPoint = calculateMidpoint(ranges[3], ranges[4]);
    if(state == "s4"):
        midPoint = calculateMidpoint(ranges[4], ranges[5]);
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

# def printEachEntry(resultProbability,week):
# 	state = getState(resultProbability,week);
# 	if(state == "s0"):
# 		return "1, 0, 0"
# 	if(state == "s1"):
# 		return "0, 1, 0"
# 	if(state == "s2"):
# 		return "0, 0, 1"
# 	# if(state == "s3"):
# 	# 	return "0, 0, 0, 1"

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
