import copy

myList = open('input2.txt', 'r').readlines()

myListSource = copy.deepcopy(myList)

gamma, epsilon = 0, 0
i, j = 0, 0
lineLength = len(myList[0].strip())
result = ""

def toDecimal(binaryNumber):
	sum, i, power = 0, 0, len(binaryNumber) - 1
	while i < len(binaryNumber):
		sum += (int(binaryNumber[i]) * 2**(power))
		power -= 1
		i += 1
	return sum


# get gamma
while i < lineLength:
	num1, num0 = 0, 0
	while j < len(myList):
		if myList[j][i] == "1":
			num1 += 1
		elif myList[j][i] == "0":
			num0 += 1
		j += 1
	if num1 > num0:
		result += "1"
	elif num0 > num1:
		result += "0"
	i += 1
	j = 0
gamma = toDecimal(result.strip())
result = ""

i, j = 0,0
# get epsilon
while i < lineLength:
	num1, num0 = 0, 0
	while j < len(myList):
		if myList[j][i] == "1":
			num1 += 1
		elif myList[j][i] == "0":
			num0 += 1
		j += 1
	if num1 > num0:
		result += "0"
	elif num0 > num1:
		result += "1"
	i += 1
	j = 0

epsilon = toDecimal(result.strip())

# print(gamma * epsilon)

# part two

# def removeLines(inputList, removeOnes, col):
# 	i = 0
# 	print(len(inputList))
# 	if removeOnes:
# 		while i < len(inputList):
# 			if inputList[i][col] == "1":
# 				print("removing " + inputList[i])
# 				inputList.pop(i)
# 			else:
# 				print("skipped " + inputList[i])
# 			i += 1
# 	else:
# 		while i < len(inputList):
# 			if inputList[i][col] == "0":
# 				# print("removing " + inputList[i])
# 				inputList.pop(i)
# 			i += 1
# 	return inputList

# oxygenRating, co2Rating, stop = 0,0, False
# i, j = 0, 0
# lineLength = len(myList[0].strip())

# # get oxygen
# while i < lineLength and not stop:
# 	num1, num0 = 0, 0
# 	if len(myList) == 1: # break condition
# 		oxygenRating = toDecimal(myList[0].strip())
# 		# print(myList[0])
# 		print("in oxygen end")
# 		stop = True
# 	elif len(myList) > 1: # get total number of ones and zeroes
# 		while j < len(myList):
# 			if myList[j][i] == "1":
# 				num1 += 1
# 			elif myList[j][i] == "0":
# 				num0 += 1
# 			j += 1
# 		if num1 > num0: # after done accumulating number of ones and zeroes, determine if there are more ones or zeroes then remove rows accordingly
# 			# if there are more ones than zeroes, remove the zeroes
# 			removeOnes = False
# 			myList = removeLines(myList, removeOnes, i)
# 		elif num0 > num1 or num0 == num1:
# 			# if there are more zeroes than ones, remove the ones. if there are equal amounts of both, remove the ones
# 			removeOnes = True
# 			myList = removeLines(myList, removeOnes, i)
# 		i += 1
# 		j = 0
# 	print(myList)

# # get co2
# i, j, stop = 0, 0, False
# myList = copy.deepcopy(myListSource) 
# lineLength = len(myList[0].strip())

# while i < lineLength and not stop:
# 	num1, num0 = 0, 0
# 	if len(myList) == 1: # break condition
# 		co2Rating = toDecimal(myList[0].strip())
# 		print(myList[0])
# 		stop = True
# 	elif len(myList) > 1:
# 		while j < len(myList):
# 			if myList[j][i] == "1":
# 				num1 += 1
# 			elif myList[j][i] == "0":
# 				num0 += 1
# 			j += 1
# 		# print("num1 is " + str(num1) + ", num0 is " + str(num0))
# 		if num0 > num1: # if there are more zeroes than ones, remove the zeroes. 
# 			removeOnes = False
# 			myList = removeLines(myList, removeOnes, i)
# 			# print("inside removeOnes")
# 		elif num1 > num0 or num1 == num0: # if there are more ones than zeroes, remove the ones. If there are equal number of both, then remove the ones.
# 			removeOnes = True
# 			myList = removeLines(myList, removeOnes, i)
# 		i += 1
# 		j = 0
# 	# print(myList)
# 	# print(str(len(myList)))

# print(oxygenRating * co2Rating)

