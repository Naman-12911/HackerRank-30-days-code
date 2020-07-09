#This problem is all about unit testing.

#For a given array of  integers, the function returns the index of the element
#with the minimum value in the array. If there is more than
#one element with the minimum value, the returned index should be the smallest one.
#If an empty array is passed to the function, it should raise an Exception.
#Note: The arrays are indexed from .


def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []
        

class TestDataUniqueValues(object):


    @staticmethod
    def get_array():
        # complete this function
        return [3,1,2]

    @staticmethod
    def get_expected_result():
        # complete this function
        return 1

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        return [3,1,1]

    @staticmethod
    def get_expected_result():
        # complete this function
        return  1
