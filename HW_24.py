m = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
res = list(map((lambda x: x.append(round(x[2]*x[3]))), m))
res2 = list(map((lambda x: x.append(x[4]+10) if x[4] < 100 else x.append(x[4])), m))
res3 = (list(map(lambda x: tuple(x[0:6:5]), m)))
print(res3)


