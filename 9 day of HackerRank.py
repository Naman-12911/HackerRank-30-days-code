#Task
#Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

#Input Format

#A single integer,  (the argument to pass to factorial).

#Output Format

#Print a single integer denoting .

#Sample Input

#3

#Sample Output

#6
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
    print(result)
