class Solution:
    def getSum(self, a: int, b: int) -> int:

        # we can convert positive numbers
        x = abs(a) 
        y = abs(b)

        #ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b,a)

        #we need to understant our process will be negative process or positive process.
        #We will use final answer
        sign = 1
        if a < 0:
            sign = -1

        if a * b >= 0:
            #sum of the positive integer numbers x+y where x > y
            #We can while iteration till the y is 0
            while y:
                answer = x^y # Bitwise XOR operator
                carry = ( x & y ) << 1 #Bitwise AND operator and left shift for additional operation
                x,y = answer, carry

        else:
            while y:
                answer = x^y #Bitwise XOR 
                borrow = ( (~x) & y ) << 1 #
                x,y = answer, borrow


        return x * sign


a = 15
b = 20
res = Solution().getSum(a, b)
print("res :", res)