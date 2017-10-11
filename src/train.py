import json
import numpy as np
from constants import *
import copy

def getNorm(a,b):
    n = len(a)
    diff = 0
    for i in range(0,n):
        diff += abs(b[i] - a[i])
    return abs(diff)

def tuRank(graph):
    n = len(graph)
    r =  np.ones((n))
    rtemp = np.zeros((n))
    graphT = np.transpose(graph)
    while True:
        rtemp = np.zeros((n))
        rnorm = 0
        # for i in range(0, n):
        #     for j in range(0,n):
        rtemp += np.matmul(graphT, r)
        rtemp += ((1-d)/(n))
        rnorm = sum(rtemp)
        rtemp /= rnorm
        print(getNorm(r,rtemp))
        if getNorm(r,rtemp) < EPSILON:
            break
        r = copy.deepcopy(rtemp)
    return rtemp

def normaliseScores(a):
    nmax = max(a)
    nmin = min(a)
    a -= nmin
    if nmax==nmin:
        return
    a /= (nmax-nmin)

if __name__ == '__main__':
    graph = np.load(MODEL_GRAPH_FILE)
        
    r = tuRank(graph)
    with open(USER_DATA) as f:
       data = json.load(f)
    
    users = [0]*len(data)
    for u in data:
        users[data[u]["pos"]] = u

    r = r[:len(users)]
    result = {}
    # print(len(r))
    # print(len(users))
    normaliseScores(r)
    print(set(r))
    for i in range(len(r)):
        result[users[i]] = r[i]
    with open(RATINGS_FILE, "w") as f:
        json.dump(result, f, indent=2)
