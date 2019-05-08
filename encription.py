
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = len(s)
    square_root = math.sqrt(n)
    #lower = math.trunc(square_root)
    upper = math.ceil(square_root)

    matrix = []
    for i in range(0, n, upper):
        if i + upper > n:
            matrix.append(s[i:n])
        else: 
            matrix.append(s[i:i+upper])

    answer = []
    temp = matrix[0:len(matrix)-1]
    for i in range(0, upper): 
        col = [x[i] for x in temp]
        answer.append(''.join(col))
        answer.append(' ')

    last_row = matrix[len(matrix) - 1]
    for i in range(0, len(last_row)): 
        idx = [x for x, n in enumerate(answer) if n == ' '][i]
        answer[idx-1] = answer[idx-1]+last_row[i]
    
    final_answer = ''.join(answer)
    return final_answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

