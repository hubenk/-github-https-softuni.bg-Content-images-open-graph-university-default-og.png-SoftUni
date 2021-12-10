day = str(input())

#if day in 'Monday Tuesday ...Fiday':

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")

#elif day in 'Saturday Sunday':

elif day == "Saturday" or day == "Sunday":
    print("Weekend")

else:
    print("Error")
