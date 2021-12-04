import copy
inputList = open('input2.txt', 'r').readlines()
myListSource = copy.deepcopy(inputList)
i = 0
print(len(inputList))

while i < len(inputList):
	if inputList[i][0] == "1":
		print("removing " + inputList[i])
		inputList.pop(i)
		i = 0
	else:
		print("skipped " + inputList[i])
	i += 1

print(inputList)
