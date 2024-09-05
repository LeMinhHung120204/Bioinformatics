fi = open('input.inp', 'r')
data = list(fi)

string1 = data[0][:len(data[0])]
string2 = data[1][:len(data[1])]

i = string1.find(string2)
count = 0

print(string2)

while(i >= 0):
    count += 1
    string_list = list(string1)
    string_list[i] = '*'
    string1 = ''.join(string_list)
    i = string1.find(string2)

print(count)
