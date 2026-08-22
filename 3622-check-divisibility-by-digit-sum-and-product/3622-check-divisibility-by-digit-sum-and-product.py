class Solution(object):
    def checkDivisibility(self, n):
        sum = 0 
        product = 1
        x = n
        while(x>0):
            digit = x % 10
            product = product * digit
            sum = sum + digit
            x = x // 10
        return n%(sum+product) == 0