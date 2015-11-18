#! /usr/bin/python
__author__ = "imrul"
__date__ = "$Nov 17, 2015 3:03:49 PM$"

import sys
import random

def generateRandomPointbyDistribution():
    randomPoint = 0.0;
    binList = list();
    binList = [15, 25, 35, 45, 55, 65, 75, 85]
    freqList = list();
    freqList = [524, 89, 38, 11, 9, 4, 2, 1];
    probList = list();
    
    
    
    totalFreq = getTotalFrequency(freqList);    
#    sys.stdout.write("total Frequency is "+ str(totalFreq)+"\n");
    probList = getProbability(freqList, totalFreq);
#    sys.stdout.write("Probability List "+ str(probList[0])+","+str(probList[1])+","+
#    str(probList[2])+","+str(probList[3])+","+str(probList[4])+","+str(probList[5])+
#    ","+str(probList[6])+","+str(probList[7])+"\n");
    randomPoint = getRandomPoint(binList, probList);
    return randomPoint;


def getProbability(freqList, totalSampleSpace):
    prob = list();
    for freq in freqList:
        prob.append(float(freq / totalSampleSpace));
    return prob;

def getTotalFrequency(freqList):
    totalFrq = 0.0
    for fre in freqList:
        totalFrq = totalFrq + fre;
    return totalFrq;

def calculateMidpoint(lowerBound, upperBound):
    return float((lowerBound + upperBound) / 2);

def getRandomPoint(binList, probList):
    randomPoint = 0.0;
    randNumber = random.random();
#    sys.stdout.write("Generated Random Number is "+str(randNumber)+"\n");
    state = 10;
    count = 0;
    lowerBound = 0.0;
    for count in range(0, len(probList)):
        upperBound = lowerBound + probList[count];
        if(count == 0):
            if(randNumber >= lowerBound and randNumber <= upperBound):
                state = count;
        else:
            if(randNumber > lowerBound and randNumber <= upperBound):
                state = count;
        if(state != 10):
            break;
        lowerBound = upperBound;    
        count = count + 1;
    randomPoint = randomPointByState(state, binList);    
    return randomPoint;

def randomPointByState(state, binList):
    lowerBound = 5.5;
#    sys.stdout.write("Chosen State is "+str(state)+"\n");
    if(state == 0):
#        sys.stdout.write("bound= "+str(lowerBound)+"-"+str(binList[state]))
        return calculateMidpoint(lowerBound, binList[state])
    else:
#        sys.stdout.write("bound= "+str(binList[state-1])+"-"+str(binList[state]))
        return calculateMidpoint(binList[state-1], binList[state]);

#rand = generateRandomPointbyDistribution();
#
#sys.stdout.write("generated random number for the last bin "+str(rand)+"\n");