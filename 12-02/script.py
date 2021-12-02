myList = open('input.txt', 'r').readlines()

# part 1
i, xPos, yPos = 0, 0, 0

while i < len(myList):
	line = myList[i].split(' ')
	if line[0][0] == 'f':
		xPos += int(line[1])
	elif line[0][0] == 'd':
		yPos += int(line[1])
	elif line[0][0] == 'u':
		yPos -= int(line[1])
	i += 1

print(yPos * xPos)

# part 2

i, yPos, xPos, aim = 0, 0, 0, 0
while i < len(myList):
	line = myList[i].split(' ')
	
	if line[0][0] == 'f':
		xPos += int(line[1])
		yPos += aim * int(line[1])
	elif line[0][0] == 'd':
		aim += int(line[1])
	elif line[0][0] == 'u':
		aim -= int(line[1])

	i += 1
print(yPos * xPos)