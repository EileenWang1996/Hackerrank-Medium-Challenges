
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):

    alphabet ={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 
                'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
                'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
                'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    number = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f',
                7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                13: 'm', 14:'n', 15: 'o', 16: 'p', 17:'q', 18:'r',
                19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y',
                26:'z'}

    temp_list = []

    for character in w: 
        temp_list.append(alphabet[character])
    
    idx = -1
  
    for i in range(len(temp_list)-1, -1, -1):
        if i == 0:
            return 'no answer'
        if temp_list[i] > temp_list[i-1]: 
            idx = i-1 
            break
    
    smallest = 27
    smallest_idx = -1

    for i in range(idx+1, len(temp_list)):
        if temp_list[i] > temp_list[idx]:
            if temp_list[i] < smallest:
                smallest = temp_list[i]
                smallest_idx = i

    temp_num = temp_list[idx]
    temp_list[idx] = smallest
    temp_list[smallest_idx] = temp_num 

    sorted_part = temp_list[idx+1:]
    sorted_part.sort()
    new_list = temp_list[:idx+1] + sorted_part 

    answer = ''
    for num in new_list:
        answer += number[num]
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

