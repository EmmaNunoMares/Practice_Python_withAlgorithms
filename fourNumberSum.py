"""
Sample input: [7,6,4,-1,1,2], 16
sample output: [[7,6,4,-1],[7,6,1,2]]
"""

def fourNumberSum(array, targetSum):
    out = []
    hashT = {}
    indexP = 1
    indexQ = indexP+1

    while indexQ <= len(array)-1:        
        indexP_sub = indexP-1
        indexQ_sub = indexQ+1
        #print("P,subP -> "+str(indexP)+","+str(indexP_sub)+ " Q,subQ -> "+str(indexQ)+","+str(indexQ_sub))
        while indexP_sub >= 0:
            sumP = array[indexP_sub] + array[indexP]
            #print("sumP "+str(sumP))
            if sumP in hashT:
                hashT[sumP].append([array[indexP_sub], array[indexP]])
            else:
                hashT[sumP] = [[array[indexP_sub], array[indexP]]]
            indexP_sub -= 1
        #print(str(indexQ_sub)+"-----------hash Table "+str(hashT))            
        while indexQ_sub <= len(array)-1:
            sumQ = targetSum - (array[indexQ_sub] + array[indexQ])
            #print("sumQ "+str(sumQ))
            if sumQ in hashT:
                for elements in hashT[sumQ]:
                    out.append([elements[0], elements[1], array[indexQ_sub], array[indexQ]])
            indexQ_sub += 1
        indexP += 1
        indexQ += 1                
    return out

array = [7,6,4,-1,1,2]
targetSum = 16
result = fourNumberSum(array, targetSum)
print(result)
