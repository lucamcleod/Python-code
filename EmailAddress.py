dic = {}

with open("phonebook.in", "r") as rf:
	for x in rf:
		dic[x.strip()] = next(rf).strip()

inp = input("Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit:")

while str(inp) != '5':
	if str(inp) == '1':
		inp_1 = input("Enter name:")
		if inp_1 in dic:
			print(dic[inp_1])
		else:
			print("Sorry, no contact exists under that name.")

	elif str(inp) == '2':
		inp_1 = input("Enter name:")
		inp_2 = input("Enter email address:")
		dic[inp_1] = inp_2
		with open("vdnjd.txt", "w") as wf:
			for key, value in dic.items():
				wf.write('\n' + key)
				wf.write('\n' + value)

	elif str(inp) == '3':
		inp_1 = input("Enter name:")
		inp_2 = input("Enter new email address:")
		dic[inp_1] = inp_2
		with open("icdjj.txt", "w") as wf:
			for key, value in dic.items():
				wf.write('\n' + key)
				wf.write('\n' + value)

	elif str(inp) == '4':
		inp_1 = input("Enter name:")
		del dic[inp_1]
		with open("ajbvj.txt", "w") as wf:
			for key, value in dic.items():
				wf.write('\n' + key)
				wf.write('\n' + value)

	inp = input("Enter\n1) look up an email address\n2) add a new name and email address\n3) change an email address\n4) delete a name and email address\n5) save address book and exit:")

else:
	with open("phonebook.out", "w") as wf:
		for key, value in sorted(dic.items()):
			wf.write(key + '\n')
			wf.write(value + '\n')