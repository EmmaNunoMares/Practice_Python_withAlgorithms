"""
Write a function that, given a string, returns its longest palindromic substring
*a palindrome is defined as a string that's written the same forward and backward
*note that a single character strings are palindrome

sample input: "abaxyzzyxf"
sample output: "xyzzyx"

Analisis:
abba  	->	ab | ba
abcba	->	ab(c)ba
"""
def longestPalindromicSubstring(string):
	currentLongest= [0,1]
	for x in range(1, len(string)):
		print("Index "+str(x))
		odd = getExpand(string, x-1, x+1, 'O')		
		even = getExpand(string, x-1, x, 'E')
		print("Expand odd: "+str(odd))
		print("Expand even: "+str(even))
		longest = max(odd, even, key=lambda i: i[1] - i[0])
		currentLongest = max(longest, currentLongest, key=lambda i: i[1] - i[0])
	return string[currentLongest[0] : currentLongest[1]]
	
def getExpand(string, leftIndx, rigthIndx, typeN):	
	while leftIndx >= 0 and rigthIndx < len(string):		
		if string[leftIndx] != string[rigthIndx]:
			break
		print(typeN+" LeftIdx: " +str(leftIndx)+" ["+str(string[leftIndx])+"]"+", RightIdx: "+str(rigthIndx)+" ["+str(string[rigthIndx])+"]")		
		leftIndx -=1
		rigthIndx +=1
	return [leftIndx+1, rigthIndx]

print(longestPalindromicSubstring("abaxyzzyxf"))	





















