class Solution:
    def getSum(self, a: int, b: int) -> int:

        def decimalToBinary(n):
            return "{0:b}".format(int(n))


        x, y = abs(a), abs(b)
        print("initial  abs(x) : ", x , " - abs(y) :", y)
        # ensure that abs(a) >= abs(b)
        if x < y:
            print("We will do reverse process")
            return self.getSum(b, a)
        
        print("================================")
        print(" a binary : ", decimalToBinary(a))
        print(" b binary : ", decimalToBinary(b))

        print(" x binary : ", decimalToBinary(x))
        print(" y binary : ", decimalToBinary(y))
        # abs(a) >= abs(b) --> 
        # a determines the sign
        sign = 1 if a > 0 else -1

        print("sign : ", sign)
        print("-----------------------------")
        
        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
               
                print(" AND : " , decimalToBinary(x & y))
                print(" XOR : " , decimalToBinary(answer))

                carry = (x & y) << 1

                print("     after shift  AND: ", decimalToBinary(carry))

                x, y = answer, carry
                print("     x : ", x , " - y :", y)
                print("-----------------------")
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                print(" We will process negative operation")
                answer = x ^ y
                borrow = ((~x) & y) << 1
                
                print(" ~ AND : " , decimalToBinary((~x) & y))
                print(" ~ AND borrow : " , decimalToBinary( ( (~x) & y) << 1))
                print(" XOR : " , decimalToBinary(answer))

                x, y = answer, borrow
                print("     x : " , decimalToBinary(x))
                print("     y : " , decimalToBinary(y))

                print("     x : ", x , " - y :", y)
                print("-----------------------")

        return x * sign


a = 15
b = 20
res = Solution().getSum(a, b)
print("res :", res)