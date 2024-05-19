import sys

src_circle = sys.argv[1]
src_points = sys.argv[2]

with open(src_circle, 'r') as file:
    def_circle = file.readlines()

stripped = [j.strip().split(' ') for j in def_circle[:-1]]

circle_x = float(stripped[0][0])
circle_y = float(stripped[0][1])
circle_r = float(def_circle[-1])

point_y = 6
point_x = 6

sq_length_x = (point_x - circle_x) ** 2
sq_length_y = (point_y - circle_y) ** 2

if sq_length_x + sq_length_y == circle_r ** 2:
    print(0)
elif sq_length_x + sq_length_y < circle_r ** 2:
    print(1)
else:
    print(2)
