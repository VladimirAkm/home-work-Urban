class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start


en = EvenNumbers(10, 24)
for i in en:
    if i % 2 == 0:
        print(i)
