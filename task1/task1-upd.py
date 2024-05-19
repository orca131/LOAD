import sys

length = int(sys.argv[1])
step = int(sys.argv[2])

x = max(length, step)
y = min(length, step)

print(max(length, step) // min(length, step))


# Сколько целых шагов можно сделать за 1 проход списка

# cur_step = 0
# cur_length = 0
# mlt_step = max(length, step) // min(length, step)

#while cur_length != cur_step:
#    cur_length += min(length, step) * mlt_step

#while length != step:
#    large_step

#result = list_ * length

#result.append(list_[0])

#print(*result, sep='')
#print(length, step)

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