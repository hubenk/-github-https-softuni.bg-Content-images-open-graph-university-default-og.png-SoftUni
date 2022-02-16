import re
initial_dates = input()

regex = r"\b(?P<days>\d{2})(?P<separator>[-/.])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"

match_date = re.finditer(regex, initial_dates)

for date in match_date:
    result = date.groupdict()
    print(f"Day: {result['days']}, Month: {result['month']}, Year: {result['year']}")

