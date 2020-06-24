#Task
#Complete the Difference class by writing the following:

#A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
#A computeDifference method that finds the maximum
#absolute difference between any  numbers in  and stores it in the  instance variable.


#Sample Input

#3
#1 2 5
#Sample OutputS

#4
class Difference:
    def __init__(self, a):
        self.__elements = a

        self.maximumDifference = 0

    def computeDifference(self):
        min_element = 101
        max_element = 0
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element

        self.maximumDifference = max_element - min_element


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifferenc


