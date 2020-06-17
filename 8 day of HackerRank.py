#Task
#Given an array, , of  integers, print
#'s elements in reverse order as a single line of space-separated numbers.

#input Format

#The first line contains an integer,  (the size of our array).
#The second line contains  space-separated integers describing array 's elements.

#Output Format

#Print the elements of array  in reverse order as a single line of space-separated numbers.

#Sample Input

#4
#1 4 3 2
#Sample Output

#2 3 4 1

 n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reversed_array = []
    for i in range (n):
        reversed_array.append(arr[n-i-1])
    output_string = ''
    for i in range (len(reversed_array)):
        output_string += str(reversed_array[i]) + ' '    
    print(output_string)    
