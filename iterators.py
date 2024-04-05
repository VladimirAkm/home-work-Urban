class EvenNumbers:
    def __init__(self, start=0, end=0):
        if start % 2 == 0:
            self.start = start
        else:
            start = start + 1
            self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        result = self.start
        self.start += 2
        return result


en = EvenNumbers(10,25)
for i in en:
    print(i)
