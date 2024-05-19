import sys

# Получить файлы с данными в качестве аргументов

src_circle = sys.argv[1]
src_points = sys.argv[2]

# Получить параметры окружности

with open(src_circle, 'r') as file:
    raw_circle = file.readlines()

# Записать координаты центра окружности в список

mid_circle = [j.strip().split(' ') for j in raw_circle[:-1]]

# Присвоить значения переменным, описывающим окружность

circle_x = float(mid_circle[0][0])
circle_y = float(mid_circle[0][1])
circle_r = float(raw_circle[-1])

# Получить координаты

with open(src_points, 'r') as file:
    raw_points = file.readlines()

# Записать координаты в список

all_points = [k.strip().split(' ') for k in raw_points]

# Определить положение точки относительно окружности
# для каждой пары координат: 
# 0 - точка лежит на окружности 
# 1 - точка внутри
# 2 - точка снаружи

for p in all_points:
    sq_length_x = (float(p[0]) - circle_x) ** 2
    sq_length_y = (float(p[1]) - circle_y) ** 2
    if sq_length_x + sq_length_y == circle_r ** 2:
        print(0)
    elif sq_length_x + sq_length_y < circle_r ** 2:
        print(1)
    else:
        print(2)
