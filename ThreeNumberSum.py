"""
Sample input: [12,3,1,2,-6,5,-8,6], 0
sample output: [[-8,2,6],[-8,3,5],[-6,1,5]]
time  -> 
space -> 
"""

def threeNumberSum(array, targetSum):
    out = []
    array.sort()
    startIndex = 0
    #print("SORT ARRAY: " + str(array))
    for num in array:
        startIndex += 1
        leftIn = startIndex
        rigthIn = len(array)-1
        #print("-------------- startIndex: "+str(startIndex)+" len "+str(len(array)-1))
        for x in range(startIndex, len(array)-1):
            test = num + array[leftIn]+ array[rigthIn]
            #print("left: "+str(leftIn)+","+str(array[leftIn])+" rigth: "+ str(rigthIn)+","+str(array[rigthIn]))
            if targetSum == test:
                #print("Bingo")
                out.append([num, array[leftIn], array[rigthIn]])
                rigthIn -= 1
                leftIn += 1
            if test > targetSum:
                rigthIn -= 1
            if test < targetSum:
                leftIn += 1
            if leftIn >= rigthIn:
                break

    return out

array = [12,3,1,2,-6,5,-8,6]
target = 0
result = str(threeNumberSum(array,target))
print(result)
