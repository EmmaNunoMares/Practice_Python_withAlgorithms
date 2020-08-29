"""
Write a function that takes in two non-empty arrays of integers, finds the pair
of numbers -one from each array- whose absolute difference is closest to zero,
and returns an array containing these two numbers, with the number from the first
array in the first position.

Sample input: [-1,5,10,20,28,3],[26,134,135,15,17]
Sample output: [28,26]

"""
import sys

"""
tiemp: O(nlog(n) + mlog(m))
space: O(1)
"""
def smallestDifference(arrayOne, arrayTwo):
    out = []
    arrayOne.sort()
    arrayTwo.sort()
    idxone = 0
    idxtwo = 0
    smallest = float("inf")
    current = float("inf")
    print("ONE: "+str(array_One))
    print("TWO: "+str(array_Two))
    while(idxone < len(arrayOne) and idxtwo < len(arrayTwo)):
        firstNum = arrayOne[idxone]
        secondNum = arrayTwo[idxtwo]
        print("first: "+str(firstNum)+" second: "+str(secondNum))		
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxone += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxtwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            out = [firstNum, secondNum]
    return out

    
array_One = [-1,5,10,20,28,3]
array_Two = [26,134,135,15,17]
result = smallestDifference(array_One, array_Two)
print("Out: " + str(result))



















