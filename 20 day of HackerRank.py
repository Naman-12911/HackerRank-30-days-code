#Task
#Given an array, , of size  distinct elements, sort the array
#in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:

#Array is sorted in numSwaps swaps.
#where  is the number of swaps that took place.
#First Element: firstElement
#where  is the first element in the sorted array.
#Last Element: lastElement
#where  is the last element in the sorted array.
#Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.



#Print the following three lines of output:

#Array is sorted in numSwaps swaps.
#where  is the number of swaps that took place.
#First Element: firstElement
#where  is the first element in the sorted array.
#Last Element: lastElement
#where  is the last element in the sorted array.

#Sample Input 0

#3
#1 2 3

#Sample Output 0

#Array is sorted in 0 swaps.
#First Element: 1

#Last Element: 3
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    currentSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numSwaps += 1
            currentSwaps += 1

    if currentSwaps == 0:
        break

print('Array is sorted in ' + str(numSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))
