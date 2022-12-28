class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.cnt = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1

        if self.cnt == self.count:
            raise StopIteration

        return self.cnt * self.step
