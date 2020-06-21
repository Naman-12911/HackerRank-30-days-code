#Task
#Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

#Input Format

#There are  lines of input, where each line contains
#space-separated integers describing 2D Array ;
#every value in  will be in the inclusive range of  to .


#Output Format

#Print the largest (maximum) hourglass sum found in .

#Sample Input

#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 2 4 4 0
#0 0 0 2 0 0
#0 0 1 2 4 0
#Sample Output

#19
if __name__ == '__main__':
    def _get_hourglass_sum(matrix, row , col):
        sum = 0
        sum += matrix[row-1][col-1]
        sum += matrix[row-1][col]
        sum += matrix[row-1][col+1]
        sum += matrix[row][col]
        sum += matrix[row+1][col-1]
        sum += matrix[row+1][col]
        sum += matrix[row+1][col+1]
        return sum
        
    arr = []

    for i in range(6):
        arr_t = [int(arr_temp)for arr_temp in input().strip().split(' ')]

        arr.append(arr_t)
    max_hourglass_sum = -63    
    for i in range(1,5):
        for j in range(1,5):
            current_hourglass_sum = _get_hourglass_sum(arr ,i , j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum    
    print(max_hourglass_sum)            
