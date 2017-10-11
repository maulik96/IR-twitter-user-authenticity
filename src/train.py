import json
import numpy as np
from constants import *
import copy

def getNorm(a,b):
    n = len(a)
    diff = 0
    for i in range(0,n):
        diff += (b[i] - a[i])
    return abs(diff)

def tuRank(graph):
    n = len(graph)
    r = [1.0]*(n)
    rtemp = [0.0]*(n)

    while (getNorm(r,rtemp) > EPSILON):
        rtemp = [0.0]*(n)
        for i in range(0, n):
            for j in range(0,n):
                rtemp[i] += graph[j][i]*r[j]
            rtemp[i] += ((1-d)/(n))
        r = copy.deepcopy(rtemp)
    return r

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
    print(len(r))
    print(len(users))
    print(set(r))
    for i in range(len(r)):
        result[users[i]] = r[i]
    with open(RATINGS_FILE, "w") as f:
        json.dump(result, f, indent=2)
