with open('input.inp','r') as fi:
    st1 = fi.readline().strip()
    st2 = fi.readline().strip()

i = 0
res = 0
while(i < len(st1)):
    if(st1[i] != st2[i]):
        res += 1
    i += 1
print(res)