"""
Write a function that takes in non-empty array of distinct integers and an integer
representating a target sum. If any two numbers in the input array sum up to the target sum
the function should return them in an array in any order. if no two numbers sum up to 
the target sum, the function should return an empty array.
Note that the target sum hast o be obtained by summing two different integers in the array
you cant add a single integer to itself in order to obtain the target sum.
Sample input: [3,5,-4,8,11,1,-1,6], 10
sample output: [-1,11]
time  -> O(n)
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
    
