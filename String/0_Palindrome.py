"""
write a fuknction that takes in a non-empty string and tat returns a boolean representing
whether the string is a polindrome.
PALINDROME: is defined as a string that's written the same forward and backward

input= "abcdcba"
output = true
"""

def isPalindrome(string):
	helper= ""
	for x in reversed(range(len(string))):
		print(x)
		helper = helper + str(string[x])
	
	return helper == string	

string = "abcdcba"	
print(isPalindrome(string))
