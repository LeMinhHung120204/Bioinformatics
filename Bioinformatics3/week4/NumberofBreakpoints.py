with open('input.inp', 'r') as fi:
    array = list(map(int, fi.readline().split()))

array.insert(0, 0)
array.append(len(array))

res = 0
for i in range(len(array) - 1):
    if array[i + 1] - array[i] != 1:
        res += 1
print(res) 