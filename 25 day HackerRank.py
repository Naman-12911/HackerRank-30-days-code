#Task
#A prime is a natural number greater than  that has no positive
#divisors other than  and itself. Given a number, , determine and print whether it's.

#Sample Input

#3
#12
#5
#7
#Sample Output

#Not prime
#Prime
#Prime
import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n%i == 0:
            return False
    return True


num_test_cases = int(input())
for i in range(num_test_cases):
    n = int(input())
    if isPrime(n):
        print('Prime')
    else:
        print('Not prime')
