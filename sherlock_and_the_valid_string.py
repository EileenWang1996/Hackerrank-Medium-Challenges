
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    if len(s) == 1 or len(s) == 2:
        return "YES"

    char_freq = {}
    for char in s: 
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    smallest = math.inf
    maximum = 0 
    for key in char_freq:
        if char_freq[key] < smallest:
            smallest = char_freq[key]
        if char_freq[key] > maximum:
            maximum = char_freq[key]
    
    count = 0
    count_max = 0
    freq = 0
    for key in char_freq:
        if char_freq[key] > smallest:
            count += 1
            freq = char_freq[key]
        if char_freq[key] < maximum:
            count_max += 1

    
    if count == 0 or (count == 1 and freq - smallest == 1) or count_max == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

