from math import ceil

movie_name = str(input())
lenght_of_episode = int(input())
lenght_of_break = int(input())

lunch = lenght_of_break / 8
free_time = lenght_of_break / 4

time_left = (lenght_of_break - (lunch + free_time))

if time_left >= lenght_of_episode:
    tottal_free_time = ceil(time_left - lenght_of_episode)
    print(f"You have enough time to watch {movie_name} and left with {tottal_free_time} minutes free time.")

else:
    not_enough_time = ceil(lenght_of_episode - time_left)
    print(f"You don't have enough time to watch {movie_name}, you need {not_enough_time} more minutes.")