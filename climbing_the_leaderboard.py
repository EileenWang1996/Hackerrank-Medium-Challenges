
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []
    scores = list(set(scores))
    scores.sort(reverse = True)
    i = len(scores) - 1 
    for alice_score in alice: 
        while i >= 0: 
            if alice_score >= scores[i]: 
                i -= 1
            else: 
                result.append(i+2)
                break
        if i < 0: 
            result.append(1) #case when alice comes first 
    return result   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input()) #number of players on leaderboard 

    scores = list(map(int, input().rstrip().split())) #leaderboard scores in descending order

    alice_count = int(input()) #number of games alice plays 

    alice = list(map(int, input().rstrip().split())) #alices scores 

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

