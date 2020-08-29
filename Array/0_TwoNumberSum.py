"""
Write a function that takes in non-empty array of distinct integers and an integer
representating a target sum. If any two numbers in the input array sum up to the target sum
the function should return them in an array in any order. if no two numbers sum up to 
the target sum, the function should return an empty array.
Note that the target sum hast o be obtained by summing two different integers in the array
you cant add a single integer to itself in order to obtain the target sum.
Sample input: [3,5,-4,8,11,1,-1,6], 10
sample output: [-1,11]
"""

"""
time  -> O(n)
space -> O(n)
"""
def twoNumberSumHasTable(array, targetSum):
    hashtableNumbers = {}
    output = []    
    for num in array:
        test = targetSum-num
        print("test: "+str(targetSum)+"+"+str(num)+": "+str(test))
        if test in hashtableNumbers:
            return [num, test]
        else:
           hashtableNumbers[num] = True
        print("hastable: " + str(hashtableNumbers))               
    return output
    
"""
time  -> O(nLog(n))
space -> O(1)
"""
def twoNumberSumSort(array, targetSum):
	array.sort()
	left = 0
	right = len(array)-1
	print(array)
	while left < right:
		currentSum = array[left] + array[right]
		print(str(array[left])+" , "+str(array[right]))
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left += 1
		elif currentSum > targetSum:
			right -= 1
	return []


array = [3,5,-4,8,11,1,-1,6]
target = 10
resultHash = str(twoNumberSumHasTable(array,target))
print("Hash: " + resultHash)
print("--------------------------------")
resultSort = str(twoNumberSumSort(array,target))
print("Sort:" + resultSort)
    
