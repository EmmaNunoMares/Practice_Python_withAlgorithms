"""
Write a function that takes in a non-empty array of distinct integers and an integer
representing a target sum. the function should find all triples in the array that sum up
to the target sum and return a two-dimensional array of all these triplets. the numbers in
each triplet should be ordered in ascending order, and the triplets themselves should be ordered in
ascending order with respect to the numbers they hold.
Sample input: [12,3,1,2,-6,5,-8,6], 0
sample output: [[-8,2,6],[-8,3,5],[-6,1,5]]
"""

"""
time  -> nlog(n) + O(n^2)
space -> O(n)
"""
def threeNumberSum(array, targetSum):
    out = []
    array.sort()    
    print("SORT ARRAY: " + str(array))
    for i in range(len(array) - 2):        
        left = i+1
        right = len(array)-1
        print("-------------- Start Round: "+str(array[i]))
        while left < right:
            test = array[i]+array[left]+array[right]
            print("left: "+str(left)+",["+str(array[left])+"] rigth: "+ str(right)+",["+str(array[right])+"]"+"   = "+test)
            if targetSum == test:
                print("Bingo")
                out.append([array[i], array[left], array[right]])
                right -= 1
                left += 1
            elif test > targetSum:
                right -= 1
            elif test < targetSum:
                left += 1  
	
    return out

array = [12,3,1,2,-6,5,-8,6]
target = 0
result = str(threeNumberSum(array,target))
print("Out: "+result)
