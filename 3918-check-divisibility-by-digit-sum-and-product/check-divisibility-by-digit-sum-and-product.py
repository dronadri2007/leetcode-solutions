class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitsum=0
        digitproduct=1
        for i in str(n):
            digitsum+=int(i)
            digitproduct*=int(i)
        return  n%(digitproduct+digitsum)==0 