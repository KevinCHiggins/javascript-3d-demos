outp = open("code.txt", "w")

i = 0

while i < 9:
	j = 0
	while j < 3:
		outp.write("pre[" + str(i) + "] * post[" + str(j) + "] + pre[" + str(i + 1) + "] * post[" + str(j + 3) + "] + pre[" + str(i + 2) + "] * post[" + str(j + 6) + "],\n")
		j = j + 1
	i = i + 3