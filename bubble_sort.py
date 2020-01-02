sortme = [9, 8, -1, 2, -3, -7, 8, 0] # List for example

print("Input: ", sortme)

list_len = len(sortme)

for i in range(list_len - 1):
	for j in range(1, list_len - i - 1):
		if sortme[j] < sortme[j+1]:
			sortme[j], sortme[j+1] = sortme[j+1], sortme[j]
			

print("Output: ", sortme)
