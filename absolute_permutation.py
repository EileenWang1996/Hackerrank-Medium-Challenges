
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermHelper(k, temp, idx, answer, i):

    if idx > 0:
        if idx <= n and answer[idx-1] == None:
            return True, idx
    else: 
        idx = k + temp[i]
        if idx <= n and answer[idx-1] == None:
            return True, idx
            
    return False, -1

def absolutePermutation(n, k):

    temp = list(range(1, n+1))
    target = [k] * n
    diff = [a - b for a, b in zip(temp, target)]
    diff2 = [a - b for a, b in zip(target, temp)]

    answer = [None] * n
    
    for i in range(0,len(diff)):
        idx = diff[i]
        found_place, final_idx = absolutePermHelper(k, temp, idx, answer, i)
        if found_place == True: 
            answer[final_idx-1] = str(temp[i])
        else:
            idx = diff2[i]
            found_place, final_idx = absolutePermHelper(k, temp, idx, answer, i)
            if found_place == False:
                return ['-1']
            else:
                answer[final_idx-1] = str(temp[i])
    
    return answer 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

