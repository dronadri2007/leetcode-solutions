class Solution:
    def reverse(self, x: int) -> int:
        if x > 0 and x%10 != 0:
            b=int((str(x)[::-1]))
        elif x > 0 and x%10 == 0:
            b=int((str(x)[-2::-1]))
        elif x < 0:
             b=-1*(int((str(-1*x)[::-1])))
        else:
            return 0
        if b < -2**31 or b > 2**31 - 1:
            return 0
        return b
