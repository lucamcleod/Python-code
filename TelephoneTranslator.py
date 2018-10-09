inp = input("Enter a phone number to be translated:")
lst = []
for x in inp:
	lst.append(x)

x = 0

while x < len(inp):
	if lst[x] == '-':
		x += 1
	elif lst[x] == 'A' or lst[x] == 'B' or lst[x] == 'C':
		lst[x] = '2'
		x += 1
	elif lst[x] == 'D' or lst[x] == 'E' or lst[x] == 'F':
		lst[x] = '3'
		x += 1
	elif lst[x] == 'G' or lst[x] == 'H' or lst[x] == 'I':
		lst[x] = '4'
		x += 1
	elif lst[x] == 'J' or lst[x] == 'K' or lst[x] == 'L':
		lst[x] = '5'
		x += 1
	elif lst[x] == 'M' or lst[x] == 'N' or lst[x] == 'O':
		lst[x] = '6'
		x += 1
	elif lst[x] == 'P' or lst[x] == 'Q' or lst[x] == 'R' or lst[x] == 'S':
		lst[x] = '7'
		x += 1
	elif lst[x] == 'T' or lst[x] == 'U' or lst[x] == 'V':
		lst[x] = '8'
		x += 1
	elif lst[x] == 'W' or lst[x] == 'X' or lst[x] == 'Y' or lst[x] == 'Z':
		lst[x] = '9'
		x += 1
	else:
		x += 1

lst = ''.join(lst)
print(lst)