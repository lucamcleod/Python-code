with open("BoyNames.txt", "r") as rfb:
	lstboy = []
	for x in rfb:
		lstboy.append(x.rstrip('\n'))

with open("GirlNames.txt", "r") as rfg:
	lstgirl = []
	for x in rfg:
		lstgirl.append(x.rstrip('\n'))

inp = input("Enter 'boy', 'girl', or 'both':")

if inp == 'boy':
	inpboy = input("Enter a boy's name:")
	for x in range(0, len(lstboy)):
		if lstboy[x] == inpboy:
			print(lstboy[x], "was a popular boy's name between 2000 and 2009.")
		else:
			x += 1
	if inpboy not in lstboy:
		print(inpboy, "was not a popular boy's name between 2000 and 2009.")

elif inp == 'girl':
	inpgirl = input("Enter a girl's name:")
	for x in range(0, len(lstgirl)):
		if lstgirl[x] == inpgirl:
			print(lstgirl[x], "was a popular girl's name between 2000 and 2009.")
		else:
			x += 1
	if inpgirl not in lstgirl:
		print(inpgirl, "was not a popular girl's name between 2000 and 2009.")

else:
	inpboy = input("Enter a boy's name:")
	for x in range(0, len(lstboy)):
		if lstboy[x] == inpboy:
			print(lstboy[x], "was a popular boy's name between 2000 and 2009.")
		else:
			x += 1
	if inpboy not in lstboy:
		print(inpboy, "was not a popular boy's name between 2000 and 2009.")

	inpgirl = input("Enter a girl's name:")
	for x in range(0, len(lstgirl)):
		if lstgirl[x] == inpgirl:
			print(lstgirl[x], "was a popular girl's name between 2000 and 2009.")
		else:
			x += 1
	if inpgirl not in lstgirl:
		print(inpgirl, "was not a popular girl's name between 2000 and 2009.")