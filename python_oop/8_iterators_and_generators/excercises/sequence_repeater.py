class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration

        result = self.sequence[self.index]
        self.index += 1
        if self.index == len(self.sequence):
            self.index = 0
        self.number -= 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
