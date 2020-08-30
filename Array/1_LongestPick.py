"""
Write a function that takes in an array of integers and returns the length of the longest
peak in the array.
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
	i = 1
	while i < len(array)-1:
		print("Peak:"+str(array[i-1])+", "+str(array[i])+", "+str(array[i+1]))
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i += 1
			continue
		leftIdx = i-2		
		print("Extend LEFT: "+str(leftIdx))
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
			print("left: "+str(array[leftIdx]))
			leftIdx -= 1
		rightIdx = i+2
		print("Extend RIGTH: "+str(rightIdx))
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
			print("right: "+str(array[rightIdx]))
			rightIdx += 1
		print("indexes: "+str(rightIdx) +", "+str(leftIdx))
		currentPeakLength = rightIdx - leftIdx -1
		out = max(out, currentPeakLength)
		i = rightIdx
		print("potential: "+ str(out))
	return out
#[1,2,3,3,4,0,10,6,5,-1,-3, 2, 3]
#[0,1,2,3,4,5, 6,7,8, 9,10,11,12]	
result = longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3])
print("out: "+str(result))













