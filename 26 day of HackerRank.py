# task
#Your local library needs your help! Given the expected and actual return dates for a library book,
#create a program that calculates the fine (if any). The fee structure is as follows:

#If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
#If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
#If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
#If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
#Input Format

#The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
#The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due dateSample Input
# input format
#9 6 2015
#6 6 2015
#Sample Output

#45

return_day, return_month, return_year = [int(e) for e in input().strip().split(' ')]
due_day, due_month, due_year = [int(e) for e in input().strip().split(' ')]
if return_year < due_year:
    print(0)
elif return_year == due_year:
    # Check the next biggest category: month
    if return_month < due_month:
        print(0)
    elif return_month == due_month:
        # Check the last category: day
        if return_day <= due_day:
            print(0)
        else:
            print(str((return_day - due_day) * 15))
    else:
        print(str((return_month - due_month) * 500))
else:
    print('10000')
