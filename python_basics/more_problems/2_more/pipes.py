volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

percentage_filled = ((pipe_1 + pipe_2) * hours) / volume * 100
percent_pipe_1 = (pipe_1 * hours) / ((pipe_1 + pipe_2) * hours) * 100
percent_pipe_2 = (pipe_2 * hours) / ((pipe_1 + pipe_2) * hours) * 100

overflow = ((pipe_2 + pipe_1) * hours) - volume

if percentage_filled <= 100:
    print(f"The pool is {percentage_filled}% full. Pipe 1: {percent_pipe_1:.2f}%. Pipe 2: {percent_pipe_2:.2f}%.")

else:
    print(f"For {hours:.2f} hours the pool overflows with {overflow} liters.")
