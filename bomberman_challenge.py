
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
   
    if n == 1: #after one second, nothing changes 
        return grid 

    r = len(grid)
    c = len(grid[0])

    if n % 2 == 0: 
        string = 'O' * c
        answer = [string] * r
        return answer
    
    new_grid = [list(x) for x in grid] #convert string to list 

    states = [new_grid] #store the states for after one second

    n = n % 4+4

    for i in range(1, n): 
        #if i is odd: explode bombs that were planted previously
        if i % 2 == 0: 
            prev_state = states[i-2]
            string = ['O'] * c
            new_grid = [string.copy() for x in range(r)] 
            for j in range(0, r):
                for k in range(0, c): 
                    pos = prev_state[j][k]
                    if pos == 'O': 
                        new_grid[j][k] = '.'
                        #explode surrounding positions
                        if j + 1 < r: 
                            new_grid[j+1][k] = '.'
                        if j - 1 >= 0: 
                            new_grid[j-1][k] = '.'
                        if k + 1 < c: 
                            new_grid[j][k+1] = '.'
                        if k - 1 >= 0: 
                            new_grid[j][k-1] = '.'
            states.append(new_grid)
        else: #even case: plant the bombs 
            string = ['.'] * c
            new_grid = [string.copy() for x in range(r)] 
            prev_state = states[i-1]
            for j in range(0, r):
                for k in range(0, c): 
                    pos = prev_state[j][k]
                    if pos == '.':
                        new_grid[j][k] = 'O' #plant the bomb
            states.append(new_grid)

    answer = states[-1]
    final_answer = [''.join(x) for x in answer]
    return final_answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

