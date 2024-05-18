import sys

length = int(sys.argv[1])
# step = int(sys.argv[2])
# list_ = [i for i in range(1, length + 1)]
step = 2
list_ = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c','a', 'b', 'c','a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c','a', 'b', 'c']
symbol = list_[0]
counter = 0
final_round = ''

step_counter = 0

for j in list_:
    final_round = final_round + str(j)
    step_counter += 1
    print('current step:', step_counter)
    print('J:', j, 'symbol:', symbol, 'counter:', counter)
    if step_counter == step:
        if counter == step:
            break
        if j == symbol:
            counter += 1
            print('test')

print(final_round)
# print("длинна:", len(final_round))

# В итоговом списке последняя буква = первая

# 'none', list_[::2]
# Как получить индекс элемента
# get_index = list_.index('a')
# print(get_index, list_[get_index]) 

#print(list_)
# print(length + step)
