with open('input.inp','r') as fi:
    st = fi.readline().strip()
print(st)

#st = input(b)
res =[0]
i = 0
while i < len(st):
    if st[i] == 'G':
        res.append(res[i] + 1)
    elif st[i] == 'C':
        res.append(res[i] - 1)
    else:
        res.append(res[i])
    i += 1

for s in res:
    print(s, end = ' ')