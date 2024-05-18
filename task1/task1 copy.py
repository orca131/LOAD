import sys

list_ = ['a', 'b', 'c']
step = 2

new_cycle = 1
for _ in range(4):
    for j in range(0, len(list_)):

        print(list_[j])
        new_cycle += 1

        if list_[j] == list_[0]:
            print('(yup)')
