class reverse_iter:

    def __init__(self, nums):
        self.nums = list(nums)

    def __iter__(self):
        return self

    def __next__(self):

        if not self.nums:
            raise StopIteration

        return self.nums.pop()

