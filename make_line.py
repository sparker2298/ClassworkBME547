def get_line(point_1, point_2, new_x):
    x1, y1 = point_1
    x2, y2 = point_2
    m = (y2 - y1) / (x2 - x1)
    new_y = m*new_x

    return new_y
