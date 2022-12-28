class vowels:

    def __init__(self, text: str):
        self.text = text

    def __iter__(self):
        return self

    def __next__(self):
        vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']

        self.text = [x for x in self.text if x in vowels]

        if not self.text:
            raise StopIteration

        return self.text.pop(0)

