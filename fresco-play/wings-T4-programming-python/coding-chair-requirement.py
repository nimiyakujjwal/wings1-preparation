"""
In this challenge, determine the minimum no. of chairs to be purchaged to accomodate all workers in a new business workroom. There is no chair at the beginning.

There will be string array of simulations. Each simulation is described by a combination of four characters: C, R, U and L.
    - C : a new employee arives in the workroom. If there is a chair available the employee takes it. Otherwise, a new one is purchased.
    - R : an employee goes to meeting room freeing up a chair.
    - U : an employee arives from a meeting room. If there is chair available the employee takes it otherwise a new one is purchased.
    - L : an employee leaves the workroom freeing up a chair.

Example:
    Given an array of string representing the simulations a = ["CRUL"]
    In this case there is only one simulation, CRUL, represented in table below:
        Action      Total       Available
            -       0           0
            C       1           0
            R       1           1
            U       1           0
            L       1           1

    - At first there is 0 chairs.
    - "C" a new employee arives in the room and one chair is purchased.
    - "R" an emplyee goes to meeting room freeing up a chair.
    - "U" an employee arrives from the meeting room and took the chair available.
    - "L" an employee leaves the workroom freeing up the chair.

    Hence, the minimum no. of chair to be purchased is one in this case. result = [1]

Function description:
    Complete the minChair() function below.
    minChair has following parameter(s):
        string simulations[n]: an array of string representing discreate simulations to process.

    returns:
        int[n]: an array of integers denoting the minimal no. of chairs required for each simulations.


Constraints:
    1<= n <= 100
    1 <= length of each simulations <= 10000

"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minChairs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY simulations as parameter.
#

def minChairs(simulations):
    # Write your code here
    results = []
    for simulation in simulations:
        total = 0
        available = 0
        for action in simulation:
            if action == "C":
                if available > 0:
                    available -= 1
                else:
                    total += 1
            elif action == "R":
                available += 1
            elif action == "U":
                if available > 0:
                    available -= 1
                else:
                    total += 1
            elif action == "L":
                available += 1
        results.append(total)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    simulations_count = int(input().strip())

    simulations = []

    for _ in range(simulations_count):
        simulations_item = input()
        simulations.append(simulations_item)

    result = minChairs(simulations)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
