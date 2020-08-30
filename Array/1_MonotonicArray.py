"""
Write a function that takes in an array of integes and returns a boolean representing
whether the array is monotonic.

An array is said to be monotonic if its elements, form left to right, are 
entirely non-increasing or entirely non-decreasing.

Sample input: [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
Sample output: true

"""
"""
Time  O(n)
Space O(1)
"""
def isMonotonic(array):    
	isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1, len(array)):
		print(str(array[i])+", "+str(array[i-1]))
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False	
	return isNonDecreasing or isNonIncreasing

arrayTest = [1,1,2,3,4,5,-5,5,6,7,8,8,9,10,11]
print(isMonotonic(arrayTest))
