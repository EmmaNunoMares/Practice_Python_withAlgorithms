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
    startRow =0
    endRow = len(array)-1
    startCol = 0 
    endCol = len(array[0])-1
    print("sR: "+str(startRow)+", eR: "+str(endRow))
    print("sC: "+str(startCol)+", eC: "+str(endCol))
    while startRow <= endRow and startCol <= endCol:
        print("--------- from "+str(startCol)+" to "+str(endCol+1))
        for col in range(startCol, endCol+1):
            print("["+str(startRow)+", "+str(col)+"] = "+str(array[startRow][col]))
            out.append(array[startRow][col])
        print("--------- from "+str(startRow+1)+" to "+str(endRow+1))
        for row in range(startRow+1, endRow+1):
            print("["+str(row)+", "+str(endCol)+"] = "+str(array[row][endCol]))
            out.append(array[row][endCol])
        print("--------- from "+str(startCol)+" to "+str(endCol))
        for col in reversed(range(startCol, endCol)):            
            print(startRow<endRow)
            if startRow<endRow:
				print("["+str(endRow)+", "+str(col)+"] = "+str(array[endRow][col]))
				out.append(array[endRow][col])
        print("--------- from "+str(startRow+1)+" to "+str(endRow))
        for row in reversed(range(startRow+1, endRow)):            
            if startCol<endCol:
				print("["+str(row)+", "+str(startCol)+"] = "+str(array[row][startCol]))
				out.append(array[row][startCol])                
        print("**********")
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -=1
    return out

sampleInput = [[ 1, 2, 3, 4],[12,13,14, 5],[11,16,15, 6],[10, 9, 8, 7]]
result = spiralTraberse(sampleInput)
print(result)
