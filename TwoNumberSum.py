"""
Sample input: [3,5,-4,8,11,1,-1,6], 10
sample output: [-1,11]
time  -> O(n*2)
space -> O(1)
"""
def twoNumberSum(array, targetSum):
    hashtableNumbers = {}
    output = []    
    for num in array:
        test = targetSum-num
        #print("test: " + str(test))
        if test in hashtableNumbers:
            return [num, test]
        else:
           hashtableNumbers[num] = True
        #print("hastable: " + str(hashtableNumbers))               
    return output

array = [3,5,-4,8,11,1,-1,6]
target = 10
result = str(twoNumberSum(array,target))
print(result)
    
