"""
Sample input: [-1,5,10,20,28,3],[26,134,135,15,17]
Sample output: [28,26]

tiemp: O(nlog(n) + mlog(m))
space: O(1)
"""
import sys
""" my version
def smallestDifference(arrayOne, arrayTwo):
    out =[]
    arrayOne.sort()
    arrayTwo.sort()
    holdValue = sys.maxsize
    leftOnePointer = 0
    leftTwoPointer = 0
    print("array 1: "+str(arrayOne)+" array 2: "+str(arrayTwo))
    while(leftOnePointer < len(arrayOne) and leftTwoPointer < len(arrayTwo)):
        computeSmallestD = arrayOne[leftOnePointer] - arrayTwo[leftTwoPointer]
        print("operation: "+str(computeSmallestD))
        if abs(computeSmallestD) < holdValue:
            holdValue = abs(computeSmallestD)
            out = [arrayOne[leftOnePointer], arrayTwo[leftTwoPointer]]
            print("hold value: "+str(holdValue))                               
        if leftOnePointer < len(arrayOne)-1 and arrayOne[leftOnePointer] < arrayTwo[leftTwoPointer]:
            leftOnePointer += 1        
        if leftTwoPointer < len(arrayTwo)-1 and arrayOne[leftOnePointer] > arrayTwo[leftTwoPointer]:
            leftTwoPointer += 1
        
    return out
"""

def smallestDifference(arrayOne, arrayTwo):
    out = []
    arrayOne.sort()
    arrayTwo.sort()
    idxone = 0
    idxtwo = 0
    smallest = sys.maxsize
    current = 0
    while(idxone < len(arrayOne) and idxtwo < len(arrayTwo)):
        firstNum = arrayOne[idxone]
        secondNum = arrayTwo[idxtwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxone += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxtwo += 1
        else:
            return [firstNum, secondNum]
        #print("smallest "+str(smallest)+" current "+str(current))
        if smallest > current:
            smallest = current
            out = [firstNum, secondNum]
    return out

    
array_One = [-1,5,10,20,28,3]
array_Two = [26,134,135,15,17]
result = smallestDifference(array_One, array_Two)
print(result)



















