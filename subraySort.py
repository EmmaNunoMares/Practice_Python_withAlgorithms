"""
Subray sort
sample input: [1,2,4,7,10,11,7,12,6,7,16,18,19]
sample output: [3,9]

examples: [1,2] -> [-1,-1]
          [2,1] -> [0,1]
          [0,1,1,2,3,5,8,13,21,34,55,89] -> [-1,-1]
"""

def subrraySort(array):
    minV = float("inf")
    maxV = float("-inf")
    leftIndex = 0    
    rigthIndex = len(array)-1
    output = [-1,-1]

    while leftIndex < rigthIndex and array[leftIndex] <= array[leftIndex+1]:
        leftIndex += 1        

    while rigthIndex > 1 and array[rigthIndex] >= array[rigthIndex-1]:        
        rigthIndex -= 1
    
    if leftIndex < rigthIndex:
        print("leftIndex: "+str(leftIndex)+", rigthIndex: "+str(rigthIndex))
        for indexH in range(leftIndex, rigthIndex+1):            
            if array[indexH] > maxV:
                maxV = array[indexH]
            elif array[indexH] < minV:
                minV = array[indexH]
        print("MAX: "+str(maxV)+", MIN: "+str(minV))
        subLefInx = 0
        subRigInx = len(array)-1
        while minV >= array[subLefInx]:
            subLefInx += 1
        while maxV <= array[subRigInx]:
            subRigInx -= 1        
            
        return [subLefInx,subRigInx]
    else:         
        return output

array = [0,1,1,2,3,5,8,13,21,34,55,89]
result = subrraySort(array)
print(result)
