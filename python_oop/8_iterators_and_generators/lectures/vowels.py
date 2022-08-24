class vowels:

    def __init__(self, random_str):
        self.random_str = random_str
        self.temp_index = -1
        self.range = len(random_str) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.temp_index < self.range:
            self.temp_index += 1
            if self.random_str[self.temp_index] in "AOEIUYaoeiuy":
                temp_index = self.temp_index
                return self.random_str[temp_index]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
