class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        tallies = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        for i in range(len(value) - 1):
            left = value[i]
            right = value[i + 1]
            if tallies[left] < tallies[right]:
                result -= tallies[left]
            else:
                result += tallies[left]
        result += tallies[value[-1]]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        try:
            int(value)
        except ValueError:
            return 'wrong type'

        return cls(int(value))
