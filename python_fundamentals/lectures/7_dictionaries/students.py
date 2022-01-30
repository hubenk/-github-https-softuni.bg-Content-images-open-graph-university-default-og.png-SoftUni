input_line = input().split(":")
course = {}
students = {}
count = 0
info_course = ""
course_list = []
while len(input_line) > 1:

    key, value, module = input_line

    if module not in course:
        course[module] = {}
    course[module][key] = value

    input_line = input().split(":")

for index in range(len(input_line)):
    info_course += input_line[index]

course_list = info_course.split("_")
info_course = " ".join(course_list)
for actual_courses in course:
    if info_course in actual_courses:
        for name, id in course[actual_courses].items():
            print(f"{name} - {id}")
