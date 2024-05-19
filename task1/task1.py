import sys
import math

length = int(sys.argv[1])
step = int(sys.argv[2])

# Найти наименьшее общее кратное

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

multiplier = lcm(length, step)

# Создать кольцевой диапазон
# (Как определить минимальный необходимый диапазон?)

ring_range = [_ for _ in range(1, length + 1)] * multiplier
ring_range.append(ring_range[0])


# Проверять каждый n элемент диапазона
# до тех пор пока первый элемент не встретится дважды

result = []
match = False
counter = 0
while not match:
    for j in ring_range[::step - 1]:
        if j == ring_range[0]:
            counter += 1
        if counter > 1:
            match = True
            break
        result.append(j)

# Передать результат в STDOUT

print(result)
