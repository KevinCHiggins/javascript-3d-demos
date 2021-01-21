outp = open("code.txt", "w")

i = 0

while i < 16:
	j = 0
	while j < 4:
		outp.write("pre[" + str(i) + "] * post[" + str(j) + "] + pre[" + str(i + 1) + "] * post[" + str(j + 4) + "] + pre[" + str(i + 2) + "] * post[" + str(j + 8) +"] + pre[" + str(i + 3) + "] * post[" + str(j + 12) + "],\n")
		j = j + 1
	i = i + 4