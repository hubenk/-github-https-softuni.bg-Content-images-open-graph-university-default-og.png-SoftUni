class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        sum_sec = seconds + self.seconds
        if sum_sec > Time.max_seconds:
            self.seconds = sum_sec - Time.max_seconds
            minutes += 1
            if sum_sec > 59:
                self.seconds -= 1
        else:
            self.seconds += seconds

        sum_min = minutes + self.minutes
        if sum_min > Time.max_minutes:
            self.minutes = sum_min - Time.max_minutes
            hours += 1
            if sum_min > 59:
                self.minutes -= 1
        else:
            self.minutes += minutes

        sum_h = hours + self.hours
        if sum_h > Time.max_hours:
            self.hours = sum_h - Time.max_hours
            if sum_h > 23:
                self.hours -= 1
        else:
            self.hours += hours

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        Time.set_time(self, 0, 0, 1)
        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
