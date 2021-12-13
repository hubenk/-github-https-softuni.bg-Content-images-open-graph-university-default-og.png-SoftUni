max_failed_marks = int(input())
fail_counter = 0
counter = 0
total_mark = 0
last_problem = ""

while True:
    problem = input()

    if problem == "Enough":

        avg_mark = total_mark / counter
        print(f"Average score: {avg_mark:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {last_problem}")
        break
    mark = int(input())

    if mark <= 4:
        fail_counter += 1
        if fail_counter == max_failed_marks:
            print(f"You need a break, {fail_counter} poor grades.")
            break

    last_problem = problem
    counter += 1
    total_mark += mark
    continue

