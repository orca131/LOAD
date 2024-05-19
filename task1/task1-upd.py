import sys

length = int(sys.argv[1])
step = int(sys.argv[2])

list_ = [i for i in range(1, length + 1)]

length = len(list_)
step = 2

# Сколько целых шагов можно сделать за 1 проход списка
large_step = max(length, step) // min(length, step)


if length > step:
    length // step

while length != step:
    for i in range(length // )
    step += step
        length += length

result = list_ * length

result.append(list_[0])

print(*result, sep='')
print(length, step)

# list_ = ['a', 'b', 'c','d', 'e', 'f','g', 'h']
# target = list_[0] > 1
# step = 2

# line = ''

# counter = 0
# while counter * step != 1:
#     for c in list_:
#         if counter > 1:
#             if list_[c] == list_[0]:
#                 counter += step

# print(line)

# list_ = ['a', 'b', 'c','d', 'e', 'f','g', 'h']