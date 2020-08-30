"""
Given a non-empty of lowercase letters and non-negative integer representing a key,
write a function that returns a new string obtained by shifting every letter
in the input string by k positions in the alphaber, where k is the key.
Note that letters should wrap around the alphabet; in the other words, the letter z
shifted by one returns the letter a.

input: 
	string = xyz, key= 2
output: zab
"""
def caesarCipherEncryptor(string, key):	
	result = ""
	temp = 0	
	for x in string:
		temp = ord(x) + key		
		while (temp>122):
			temp = temp-122+96			
		result = result + str(chr(temp))	
	return result

string = "xyz"	
key = 2
print(caesarCipherEncryptor(string,key))
