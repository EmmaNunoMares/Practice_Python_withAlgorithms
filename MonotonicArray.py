"""
monotonic = from left to right, are entirely non-increasing or entirely non-decreasing

Sample input: [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
Sample output: true

Time  O()
Space O()
"""

def isMonotonic(array):    
    if len(array)>= 2:
        increase = array[0] >= array[len(array)-1]                
        indxL = 0
        for indxR in range(1, len(array)):
            #print(" "+str(array[indxL])+", "+str(array[indxR]))
            if increase and array[indxL] < array[indxR]:                
                return False
            elif increase != True and array[indxL] > array[indxR]:                
                return False
            indxL += 1    
    return True

arrayTest = [1,1,2,3,4,5,5,5,6,7,8,8,9,10,11]
print(isMonotonic(arrayTest))
