
'''

For each faulty program

Exam-First/Last
Score(avg) 
s
s
method m m m m


Conclusion graph 

Score(avg)
s
s
method m m m m


'''


import csv
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

def getFileNames(path):
    fileNames = [f for f in listdir(path) if isfile(join(path, f))]
    return fileNames


def getInfo(fileName):
    method_first_dict = {}
    method_last_dict = {}

    with open(fileName,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #collect score based on the first exam scoring 
            if(row['Family']=='sbfl' and row['ScoringScheme']=='first'):
                if(row['Formula'] not in method_first_dict):
                    method_first_dict[row['Formula']] = []
                method_first_dict[row['Formula']].append(row['Score'])

            if(row['Family']=='sbfl' and row['ScoringScheme']=='last'):
                if(row['Formula'] not in method_last_dict):
                    method_last_dict[row['Formula']] = []
                method_last_dict[row['Formula']].append(row['Score'])

    return method_first_dict, method_last_dict

def graphGenerator(path):
    fileNames = getFileNames(path)
    for fileName in fileNames:
        





