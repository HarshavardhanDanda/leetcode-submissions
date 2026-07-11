class Solution:
    def sumSquare(self, n):
        sum=0
        while(n):
            k=n%10
            sum+=k**2
            n=n//10
        return sum

    def isHappy(self, n: int) -> bool:
        li=[]
        while(n):
            if(n == 1):
                return True
            li.append(n)
            n=self.sumSquare(n)
            if n in li:
                return False


        