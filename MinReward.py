"""
you have a list of student scores on the final exam in a particular order(not necessaryly sorted).
and you want to reward your students following two rules.

*all student must receive strictly one reward
*any given student must receive strictly more rewards than a adjacent student(next to left or right)
	with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score.
Sample input: 		[8,4,2,1,3,6,7,9,5]	
Sample output: 25 //[4,3,2,1,2,3,4,5,1]
"""
"""
My version didn't work
def minRewards(scores):
	rewards = []
	indexhelper = 1
	counterAsc = 0
	counterDesc = 0
	while indexhelper < len(scores):
		#print(str(scores[indexhelper-1])+" "+str(scores[indexhelper]))
		numLeft = scores[indexhelper-1]
		numRigth = scores[indexhelper]		
		if numLeft > numRigth:
			counterDesc = counterDesc + 1
			if counterAsc !=0 :
				rewards.append(getParcialRewardH(indexhelper,len(scores)))
				rewards.append(getParcialReward(2,counterAsc,2))
				counterAsc = 0 			
		if numLeft < numRigth:
			counterAsc = counterAsc + 1
			if counterDesc !=0 :
				rewards.append(getParcialRewardH(indexhelper,len(scores)))
				rewards.append(getParcialReward(2,counterDesc,2))
				counterDesc = 0
		#print(str(counterAsc)+" "+str(counterDesc))	
		indexhelper = indexhelper+1
	#print(str(counterAsc)+" y "+str(counterDesc))	
	rewards.append(getParcialReward(0,counterAsc,1))
	rewards.append(getParcialReward(0,counterDesc,1))				
	return sum(rewards)

def getParcialRewardH(index, sizeA):
	#print(str(index)+" ++++++ "+str(sizeA))
	if index == sizeA-1:
		return 0
	return 1

def getParcialReward(startN,counter,incrementCounter):
		parcialResult = 0
		if counter!=0:
			for n in range(startN, counter+incrementCounter):
				#print("n "+str(n))
				parcialResult = parcialResult+n
		#print("parcial "+str(parcialResult))
		return parcialResult
"""
def minRewards(scores):
	rewards = [1 for _ in scores]
	#print(scores)
	#print(rewards)
	#print("-------")
	for i in range(1, len(scores)):
		#print(str(i)+" -> "+str(scores[i]) + " " + str(scores[i-1]))
		if scores[i] > scores[i-1]:
			#print(str(i)+"*** " + str(rewards[i])+ " " + str(rewards[i-1]))
			rewards[i] = rewards[i-1] + 1
			#print("rewards: "+ str(rewards))

	#print("-------")
	for i in reversed((range (len(scores)-1))):
		#print(str(i)+" -> "+str(scores[i]) + " " + str(scores[i+1]))
		if scores[i] > scores[i+1]:
			#print(str(i)+"*** " + str(rewards[i])+ " " + str(rewards[i+1]+1))
			rewards[i] = max(rewards[i], rewards[i+1]+1)
			#print("rewards: "+ str(rewards))
	
	#print("-------")
	#print(rewards)
	return sum(rewards)
		
scores = [8,4,2,1,3,6,7,9,5]
out = minRewards(scores)		
print(out)



























