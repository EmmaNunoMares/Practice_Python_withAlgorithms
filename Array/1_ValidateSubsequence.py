"""
Given two non-empty arrays of integers, write a funtion that determines 
whether the second array is a subsequence of the first one
A subsequence of an array is a set of numbers that aren't necessaryly 
adjacent in the array but that are in the same order as they apper in the array
Example [1,3,4] form a subsequence of the array [1,2,3,4], and so do the numbers [2,4]
note that a single number in an array and the array itself are both valid subsequences
of the array.

Sample input: array[5,1,22,25,6,-1,8,10] sequence[1,6,-1,10]
Sample out:true
"""
#print("sequence size: "+str(sequeSize)+" index helper: "+str(indexHelper)+" array element: "+str(x)+" sequence number: "+str(sequence[indexHelper]))
#print("sequence size: "+str(len(sequence))+" index helper: "+str(indexHelper))

#O(n) time | O(1) space
def isValidSubsequence(array, sequence):
	indexHelper = 0
	sequeSize = len(sequence)
	for x in array: 				
		if indexHelper < sequeSize and x == sequence[indexHelper]:			
			indexHelper =  indexHelper+1				
	return indexHelper==sequeSize
	
array = [5,1,22,25,6,-1,8,10] 
sequence = [1,6,-1,10]
outSample = isValidSubsequence(array, sequence)
print(outSample)
