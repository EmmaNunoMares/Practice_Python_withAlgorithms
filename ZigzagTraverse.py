"""
"""

def solutions(S, A):
	hashtableNumbers = {}
	zeroN = findZero(A)
	print("0: "+str(zeroN))
	emma = ""
	for x in range(0, len(A)):
		print(str(S[A[zeroN]]))
		
		
		if A[zeroN] in hashtableNumbers:
			return emma
		else:
			hashtableNumbers[A[zeroN]] = True
		emma =  emma + str(S[A[zeroN]])
		zeroN = A[zeroN]
	return emma
	
def findZero(A):
	x = 0
	for element in A:
		if element == 0:
			return x
		x=x+1
	
S= "bytdag"	
A=[4,3,0,1,2,5]
print(solutions(S,A))
print(int("10"))

for x in range(0,len("5500"),2):
	print(x)
