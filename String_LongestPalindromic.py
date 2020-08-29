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
""" my version didnt work properly
def longestPalindromicSubstring(string):	
	stringRange = range(0,len(string))
	temHelper = ""
	for x in stringRange:				
		conExp = True
		inExp = 1
		while conExp:			
			if x-inExp in stringRange and x+inExp in stringRange:
				subStriP = string[x-inExp:x+inExp+1]
				if string[x-inExp] == string[x+inExp] and len(subStriP) > len(temHelper):
					temHelper = subStriP									
				inExp = inExp+1							
			else:
				conExp = False
		conExp = True
		inExp = 0
		while conExp:
			if x-inExp in stringRange and x+inExp+1 in stringRange:
				if string[x-inExp] == string[x+inExp+1] and len(string[x-inExp:x+inExp+1+1]) > len(temHelper):
					temHelper = string[x-inExp:x+inExp+1+1]
				inExp = inExp+1							
			else:
				conExp = False
	return temHelper
"""	
def longestPalindromicSubstring(string):
	currentLongest= [0,1]
	for x in range(1, len(string)):
		odd = getHelper(string, x-1,x+1)
		even = getHelper(string, x-1,x)
		longest = max(odd, even, key=lambda i: i[1] - i[0])
		currentLongest = max(longest, currentLongest, key=lambda i: i[1] - i[0])
	return string[currentLongest[0] : currentLongest[1]]
	
def getHelper(string, leftIndx, rigthIndx):
	while leftIndx >= 0 and rigthIndx < len(string):
		if string[leftIndx] != string[rigthIndx]:
			break
		leftIndx -=1
		rigthIndx +=1
	return [leftIndx+1, rigthIndx]

print(longestPalindromicSubstring("abaxyzzyxf"))	





















