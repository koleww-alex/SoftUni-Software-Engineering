class countdown_iterator:

    def __init__(self, start: int):
        self.start = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1

        if self.start < 0:
            raise StopIteration

        return self.start
