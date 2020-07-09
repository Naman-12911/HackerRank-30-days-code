#Task
#Consider a database table, Emails, which has the attributes First Name and Email ID.
#Given  rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in .

#Sample Input

#6
#riya riya@gmail.com
#julia julia@julia.me
#julia sjulia@gmail.com
#julia julia@gmail.com
#samantha samantha@gmail.com
#tanya tanya@gmail.com
#Sample Output

#julia
#julia
#riya
#samantha
#tanya

import sys
import random
import math
import os


if __name__ == '__main__':
    N = int(input())
    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    firstNamesList = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if regex.search(emailID):
            firstNamesList.append(firstName)
    firstNamesList.sort()
    for name in firstNamesList:
        print(name)        
