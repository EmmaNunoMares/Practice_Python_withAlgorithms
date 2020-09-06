"""
Write a function that takes in an array of strings and groups anagrams together.
Anagrams are strings made up of exactly the same letters, where orders doesn't matter.
For example "cinema" and "iceman" are anagrams; similarly "foo" and "ofo" are anagrams

your function should retun a list of anagram groups in no particular order.
 Input: 
 words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
 Output:
 [["yo", "oy"], ["act", "tac", "cat"], ["flop", "olfp"], ["foo"]]
 
"""

def groupAnagrams(words):
	hashAnagram = {}
	for w in words:
		tempW = ''.join(sorted(w))
		if tempW in hashAnagram:			
			tempList = [] + hashAnagram.get(tempW)
			tempList.append(w);
			hashAnagram[tempW] = tempList
		else:
			hashAnagram[tempW] = [w]
		
	return list(hashAnagram.values())
	
	
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
