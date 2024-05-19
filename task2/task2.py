#import sys

point_y = 6
point_x = 6
circle_x = 1
circle_y = 1
circle_r = 5

sq_length_x = (point_x - circle_x) ** 2
sq_length_y = (point_y - circle_y) ** 2

if sq_length_x + sq_length_y == circle_r ** 2:
    print(0)
elif sq_length_x + sq_length_y < circle_r ** 2:
    print(1)
else:
    print(2)
