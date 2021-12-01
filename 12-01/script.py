list = []

file = open("in.txt", "r")
for line in file:
	list.append(line)

file.close()

i = 0
counter = 0

while i + 3 < len(list):
	sum1 = int(list[i]) + int(list[i+1]) + int(list[i+2])
	sum2 = int(list[i+1]) + int(list[i+2]) + int(list[i+3])

	if sum1 < sum2:
		counter += 1
	i += 1

print(counter)