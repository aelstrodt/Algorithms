"""
    Problem: 3 sum closest
    
    Given an array S of n integers, find three integers in S 
    such that the sum is closest to a given number, target. 
    Return the sum of the three integers. You may assume that each
    input would have exactly one solution.
    
    For example, given array S = {-1 2 1 -4}, and target = 1.

    The 3sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
"""

# Approach 1: find all 3 sums in array and find the one closest to target -> itertools.combinations

from itertools import combinations
def sum_3_closest_naive(S, target):
    combs_book = dict(((abs(target - sum(combo)), combo) for combo in combinations(S,3))
    return sum(combs_book[min(combs_book)])

# Approach 2: sort the array first and choose three values to sum selectively
# Start with i = 0, j = i + 1 and k = len(S) - 1
# if the sum < target: increaase j
# if sum > target: decrease k 
# if sum == target: return sum
# using this method we are not summing all possible combinations
# however it is guaranteed that the closest sum to target will be
# one of the sums we did calculate
# O(nlogn) time complexity to sort array
# for and while loop are faster than O(n^2) 

def sum_3_closest(S, target):
    sums = []
    n = len(S)
    S.sort()
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j < k:
            c_sum = S[i] + S[j] + S[k]
            if c_sum > target:
                k -= 1
            elif c_sum < target:
                j += 1
            else:
                pass
                return c_sum
            sums.append(c_sum)
    return min(sums, key = lambda x: abs(target - x))

# Import some modules for testing
import time
import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    cases = [(random.sample(range(200),i), random.randint(-100,100)) for i in range(3,200)]
    approach_1_times = []
    approach_2_times = []
    for case in cases:
        temp_times = []
        for _ in range(3):
            time1 = time.time()
            sum_3_closest_naive(case[0], case[1])
            time2 = time.time()
            temp_times.append(time2 - time1)
        approach_1_times.append(sum(temp_times)/3)
    for case in cases:
        temp_times = []
        for _ in range(3):
            time1 = time.time()
            sum_3_closest(case[0], case[1])
            time2 = time.time()
            temp_times.append(time2 - time1)
        approach_2_times.append(sum(temp_times)/3)
    plt.plot(approach_1_times)
    plt.plot(approach_2_times)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.legend(['Approach 1', 'Approach 2'], loc = 'upper left')
    plt.title('Runtime for n values in arry')
