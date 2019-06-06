
'''

For each faulty program

Exam-First/Last
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

PWD="/Users/chiyucheng/Desktop/code/faultLocalization/results/"
PLOT="/Users/chiyucheng/Desktop/code/faultLocalization/plots/"

overall_first =  {'muse':[],
                  'ochiai':[],
                  'barinel':[],
                  'opt2':[],
                  'tarantula':[],
                  'jaccard':[],
                  'dstar2':[]
                    }
overall_last = {'muse':[],
                  'ochiai':[],
                  'barinel':[],
                  'opt2':[],
                  'tarantula':[],
                  'jaccard':[],
                  'dstar2':[]
                    }


def getFileNames(path):
    fileNames = [f for f in listdir(path)]
    return fileNames


def getInfo(fileName):
    print("get file info "+ fileName)
    method_first_dict = {}
    method_last_dict = {}

    with open(fileName,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #collect score based on the first exam scoring 
            if(row['Family']=='sbfl' and row['ScoringScheme']=='first'):
                if(row['Formula'] not in method_first_dict):
                    method_first_dict[row['Formula']] = []
                method_first_dict[row['Formula']].append(float(row['Score']))

            if(row['Family']=='sbfl' and row['ScoringScheme']=='last'):
                if(row['Formula'] not in method_last_dict):
                    method_last_dict[row['Formula']] = []
                method_last_dict[row['Formula']].append(float(row['Score']))

    return method_first_dict, method_last_dict

def graphGenerator(path,name):
    path = path+name+"/"
    fileNames = getFileNames(path)
    count = len(fileNames)

    dict_items_first = {'muse':[],
                  'ochiai':[],
                  'barinel':[],
                  'opt2':[],
                  'tarantula':[],
                  'jaccard':[],
                  'dstar2':[]
                    }
    dict_items_last = {'muse':[],
                  'ochiai':[],
                  'barinel':[],
                  'opt2':[],
                  'tarantula':[],
                  'jaccard':[],
                  'dstar2':[]
                    }

    for fileName in fileNames:
        if(fileName == '.DS_Store'):
            continue
        first_info,last_info = getInfo(path+fileName)
        #print("file name is "+ fileName)
        #print(first_info)
        
        for key in first_info:
            #print("key is " + key)
            dict_items_first[key].append(np.mean(first_info[key]))
            overall_first[key].append(np.mean(first_info[key]))
            dict_items_last[key].append(np.mean(last_info[key]))
            overall_last[key].append(np.mean(last_info[key]))
    getGraph(dict_items_first,dict_items_last,name)

def getGraph(dict_items_first,dict_items_last,name):
    
    #Calculat the average score for all bugs
    for key in dict_items_first:
        dict_items_first[key] = np.mean(dict_items_first[key])
        dict_items_last[key] = np.mean(dict_items_last[key])
    print(dict_items_first)
    print(dict_items_last)
    
    #Get the data for graph
    names = []
    first = []
    last = []

    for key in dict_items_first:
        names.append(key)
        first.append(dict_items_first[key])
        last.append(dict_items_last[key])
    
    #Generate graph
    barWidth = 0.3
    r1 = np.arange(len(first))
    r2 = [x + barWidth for x in r1]

    plt.bar(r1, first, width = barWidth, color = 'blue', edgecolor = 'black', label='first')
    plt.bar(r2, last, width = barWidth, color = 'cyan', edgecolor = 'black', label='last')

    plt.xticks([r + barWidth for r in range(len(first))], names)
    plt.ylabel('AccuracyScore(avg)')
    plt.legend()
    plt.title(name)
    #plt.show()
    plt.savefig(PLOT+name+".png")
    plt.close()


def runner():
    methods = getFileNames(PWD)
    print(methods)
    for method in methods:
        if(method == ".DS_Store"):
            continue
        graphGenerator(PWD,method)
    getGraph(overall_first,overall_last,"overall")


runner()