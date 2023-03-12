



line_counts = []
for i in range(1, 4):
	with open(f'{i}.txt') as f:
		n_line = 0

		for line in f.readlines():
			n_line += 1
		line_counts.append(n_line)

st = ''
sm = sum(line_counts)
while st.count('\n') < sm-1:
	with open(f'{line_counts.index(min(line_counts))+1}.txt') as f:
		line_counts.pop(line_counts.index(min(line_counts)))
		for line in f.readlines():
			st += line.replace('\n', '') + '\n'
print(st)














