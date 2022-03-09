def Decompresser(ch):
	chd = ""
	v = False
	while not v:
		x = int(ch[1:ch.find(" ")])
		for i in range(x):
			chd += ch[0]
		ch = ch[ch.find(" ")+1:len(ch)]
		v = ch.find(" ") == -1
	x = int(ch[1:len(ch)])
	for i in range(x):
		chd += ch[0]
	return chd

print(Decompresser("a5 b3 C4"))
