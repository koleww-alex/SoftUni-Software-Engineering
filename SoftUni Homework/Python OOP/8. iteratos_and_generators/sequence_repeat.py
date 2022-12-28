class sequence_repeat:

    def __init__(self, sequence: str, repeat: int):
        self.sequence = sequence
        self.repeat = repeat
        self.cnt = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1

        if self.cnt == self.repeat:
            raise StopIteration

        return self.sequence[self.cnt % len(self.sequence)]

