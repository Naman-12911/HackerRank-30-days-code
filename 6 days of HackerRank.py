#Given a string, , of length  that is indexed from  to ,
#print its even-indexed and odd-indexed characters as
#space-separated strings on a single line.

#Note:  is considered to be an even index.

#Input Format

#The first line contains an integer,  (the number of test cases).
#Each line  of the  subsequent lines contain a String, .

#Output Format

#For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

#Sample Input

#2
#Hacker
#Rank
#Sample Output

#Hce akr
#Rn ak
#num_test_cases = int(input())

for i in range (num_test_cases):
    test_string = input()
    even_indexed_charcters = ''
    odd_indexed_charcters = ''

    for j in range (len(test_string)):
        if j % 2 == 0:
            even_indexed_charcters += test_string[j]
        else:
            odd_indexed_charcters += test_string[j]
    print("{} {}".format(even_indexed_charcters, odd_indexed_charcters))  
