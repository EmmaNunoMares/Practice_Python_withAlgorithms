"""
You are given an array of integers and an integer. write a function that
moves all instances of that integer in the array to the end of the array
and returns the array.
the function should perform this in place it should mutate the input array
and doesnt need to maintain the order of the other integers.

Sample input: [2,1,2,2,2,3,4,2], 2
Sample output: [1,3,4,2,2,2,2,] (the element 1,3,4 could be ordered differently)

"""
"""
time -> O(n)
space-> O(1)
"""
def moveElementToEnd(array, toMove):    
    left = 0
    right = len(array)-1
    while left < right:       
        while left < right and array[right] == toMove:            
            right -= 1                    
        if(array[left] == toMove):
            array[left] = array[right]
            array[right] = toMove
        left += 1		 
    return array

array = [2,1,2,2,2,3,4,2]
toMove = 2
result = moveElementToEnd(array, toMove)
print(result)
