
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):

    containers_cap = []
    types = [0] * len(container)
    for i in range(0, len(container)):
        containers_cap.append(sum(container[i]))
        for j in range(0, len(container[i])): 
            types[j] += container[i][j]
    containers_cap.sort()
    types.sort()
    if containers_cap == types:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

