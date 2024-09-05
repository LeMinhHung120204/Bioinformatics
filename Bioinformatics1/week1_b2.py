with open('input.inp') as fi:
    string = fi.readline().strip()
    k = int(fi.readline().strip())

freqMap = {}

for i in range(len(string)- k + 1):
    st = string[i : i + k]
    if(st in freqMap):
        freqMap.update({st : freqMap[st] + 1})
    else:
        freqMap.update({st : 1})

maxx = 0
for freq in freqMap.values():
    maxx = maxx if maxx >= freq else freq

for freq in freqMap:
    if freqMap[freq] == maxx:
        print(freq)