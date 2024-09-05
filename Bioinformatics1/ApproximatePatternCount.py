with open('input.inp', 'r') as fi:
    st1 = fi.readline().strip()
    st2 = fi.readline().strip()
    d = int(fi.read())

def check(a, b, x):
    dem = 0
    for i in range(len(a)):
        if(a[i] != b[i + x]):
            dem += 1
        if(dem > d):
            return False
    return True

i = 0
res = 0
for i in range(len(st2) - len(st1) + 1):
    dem = 0
    if(check(st1, st2, i)):
        res += 1
print(res)