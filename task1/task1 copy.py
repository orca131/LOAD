import sys

list_ = ['a', 'b', 'c','d', 'e', 'f','g', 'h']
target = list_[0] > 1
step = 2

line = ''

for i in range(len(list_)):
    line += list_[i]
    if list_[i] == target and i :
        break
print(line)