class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.cnt = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1

        if self.cnt == len(self.items):
            raise StopIteration

        return self.items[self.cnt]
