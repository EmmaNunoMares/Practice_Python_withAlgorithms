"""
A peak is defined as adjacent intgers in the array that are strcictly increasing until they reach a tip the highest value in the peak,
at which point they become strictly decreasing. at least 3 integers are required to form a peak

sample input: [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
sample output: 6 //0,10,6,5,-1,-3

TestCases:
input:[1,2,3,4,5,1]
out:6
"""

def longestPeak(array):
	out = 0
	holdHighestValue = 3
	if len(array) >= 3:
		for index in range(2,len(array)):
			firstIndex = index-2
			middleIndex = index-1
			if array[middleIndex] > array[firstIndex] and array[middleIndex] > array[index]:
				tempValue = 3
				for helpIndx in range(index+1,len(array)):					
					if array[helpIndx-1] >= array[helpIndx]:
						tempValue = tempValue+1
					else:
						break
				if tempValue > holdHighestValue:
					holdHighestValue = tempValue
				out = holdHighestValue						
				
				#print(out)	
				#print(str(array[firstIndex]) +" "+ str(array[middleIndex]) +" "+ str(array[index]))
	return out
	
result = longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3])
print(result) 	
