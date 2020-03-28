"""
Sample input: [2,1,2,2,2,3,4,2], 2
Sample output: [1,3,4,2,2,2,2,] (the element 1,3,4 could be ordered differently)
time -> O(n)
space-> O(1)
"""

def moveElementToEnd(array, toMove):    
    leftIdx = 0
    rigthIdx = len(array)-1
    while(leftIdx < rigthIdx):        
        while (array[rigthIdx] == toMove and rigthIdx >=0):            
            rigthIdx -= 1            
        while (array[leftIdx] != toMove and leftIdx < len(array)-1):            
            leftIdx += 1            
        if leftIdx >= rigthIdx:
            return array
        if(array[leftIdx] == toMove):
            array[leftIdx] = array[rigthIdx]
            array[rigthIdx] = toMove
    return array

array = [1,2,4,5,6]
toMove = 3
result = moveElementToEnd(array, toMove)
print(result)
