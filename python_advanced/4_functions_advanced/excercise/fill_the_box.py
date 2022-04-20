def fill_the_box(height, length, width, *args):
    cube_volume = height * length * width
    cubes_count = 0
    for arg in args:
        if arg == "Finish":
            if cube_volume > cubes_count:
                return f"There is free space in the box. You could put {cube_volume - cubes_count} more cubes."
            return f"No more free space! You have {cubes_count - cube_volume} more cubes."
        else:
            cubes_count += arg


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
