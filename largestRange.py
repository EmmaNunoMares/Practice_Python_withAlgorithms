"""
Find the lasgest range consecutive in Array
Sample input: [1,11,3,0,15,5,2,4,10,7,12,6]
Sample output: [0,7]

#list = [1,11,3,0,15,5,2,4,10,7,12,6]
#list = [1]
#list = [1,2]
list = [8,4,2,10,3,6,7,9,1]
def largestRange(array):
    output = []
    array.sort()
    counter = 0
    biggerNumber = 0
    
    if(len(array) == 1):
        output = [array[0], array[0]]
        return output    
    print(array)
    for x in range(1, len(array)):
        firstNumber = array[x-1]
        secondNumber = array[x]

        if (abs(secondNumber) - abs(firstNumber)) == 1:
            counter += 1
        else:            
            if(counter > biggerNumber | biggerNumber == 0):
                print("counter: " + str(counter))
                biggerNumber = counter
                counter = 0
                print("out 0: " + str(x-1-biggerNumber) + " out 1: " + str(x-1))
                output = [array[x-biggerNumber-1] , array[x-1]]

    if(counter > biggerNumber):
        output = [array[len(array)-counter-1] , array[len(array)-1]]
    if(len(output) == 0):
        output = [array[0], array[len(array)-1]]
    
        
    return output
print(largestRange(list))
"""
"""
Best Solution
O(n) time
O(n) space
"""
def largestRange(array):
    bestRange = []
    longestLength = 0
    hashTableNumbers = {}
    """ hashTableNumbers
    { 1: True, 11: True,  3: True, 0: True,
     15: True,  5: True,  2: True, 4: True,
     10: True,  7: True, 12: True, 6: True}
    """
    for num in array:
        hashTableNumbers[num] = True

    for num in array:
        print("Key: "+ str(num) +" value: " + str(hashTableNumbers[num]))
        if not hashTableNumbers[num]:
            continue
        hashTableNumbers[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        
        while left in hashTableNumbers:
            print(" while left: " + str(left) + " current: " + str(currentLength))
            hashTableNumbers[left] = False
            currentLength += 1
            left -= 1
            
        while right in hashTableNumbers:
            print(" while right: " + str(right) + " current: " + str(currentLength))
            hashTableNumbers[right] = False
            currentLength += 1
            right += 1
        print("hashTable: ")            
        print(hashTableNumbers)            
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left+1, right-1]
            print(bestRange)                
    return bestRange

list = [1,11,3,0,15,5,2,4,10,7,12,6]
print(largestRange(list)) 




















    
