#Task
#Given set . Find two integers,  and  (where ), from set  such that the value of
#is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

#Input Format

#The first line contains an integer, , the number of test cases.
#Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectivelySample Input
#Input format
#3
#5 2
#8 5
#2 2
#Sample Output

#1
#4
#0
import math
import os
import random
import re
import sys

def find_max_bitwise(n,k):
    max_bitwise = 0
    for i in range(1,n+1):
        for j in range(1,i):
            bitwise = i & j
        
            if max_bitwise < bitwise < k:
                max_bitwise  = bitwise
                if max_bitwise  == k - 1:
                    return max_bitwise
    return max_bitwise            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(find_max_bitwise(n,k))

