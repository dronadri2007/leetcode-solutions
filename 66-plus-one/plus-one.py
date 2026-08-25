class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0

        for i in range(len(digits)):
            c += digits[len(digits) - 1 - i] * (10 ** i)

        b = str(c + 1)
        d = [int(i) for i in b]

        return d