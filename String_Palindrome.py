"""
write a fuknction that takes in a non-empty string and tat returns a boolean representing
whether the string is a polindrome.
PALINDROME: is defined as a string that's written the same forward and backward

input= "abcdcba"
output = true
"""

def isPalindrome(string):
	helper= ""
	for x in range(len(string)-1,-1,-1):
		helper = helper + str(string[x])
	if helper == string:
		return True		
	return False

string = "abcdcba"	
print(isPalindrome(string))
