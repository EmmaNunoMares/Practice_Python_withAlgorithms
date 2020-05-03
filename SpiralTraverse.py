"""
Spiral Traverse
Write a function that takes a matrix and returns a one-dimensional array
of all the array's elements in spiral order

Sample input = [[ 1, 2, 3, 4],
                [12,13,14, 5],
                [11,16,15, 6],
                [10, 9, 8, 7]]
Sample output = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
TestCase
input = [[ 1, 2, 3, 4],
         [10,11,12, 5],
         [ 9, 8, 7, 6]]
"""

def spiralTraberse(array):    
    out = []
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    #print(str(startRow)+ str(endRow))
    #print(str(startCol)+ str(endCol))
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol+1):
            #print(str(startRow)+" "+str(col))
            out.append(array[startRow][col])
        #print("---------")
        for row in range(startRow+1, endRow+1):
            #print(str(row)+" "+str(endCol))
            out.append(array[row][endCol])
        #print("---------") 
        for col in reversed(range(startCol, endCol)):
            #print(str(endRow)+" "+str(col))
            #print(startRow<endRow)
            if startRow<endRow:
                out.append(array[endRow][col])
        #print("---------")
        for row in reversed(range(startRow+1, endRow)):
            #print(str(row)+" "+str(startCol))
            if startCol<endCol:
                out.append(array[row][startCol])
        #print("**********")
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -=1
    return out

input = [[1,2,3,4],[10,11,12,5],[9,8,7,6]]
result = spiralTraberse(input)
print(result)
