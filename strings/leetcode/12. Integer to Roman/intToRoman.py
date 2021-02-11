'''
	We  need to keep in an data structuer like in array uniqe roman symbol and mathing number
	like 1000 > M 
	but we need 900 because is a unique.
	we can iterate in these roman numerals.
		we can check if less then we need to do action.
			
			we need a divison how many time :
				division = int(num/value)
				division = int(478/400) = 1

			and what is our new number
				num = num - value * division
				num = 478 - 400 * 1 = 78

			result.append(symbol * division)
			for result is getting from digits array. and result = "CD"


'''
class Solution:
    def intToRoman(self, num: int) -> str:

    	digits = [
    	(1000,"M"), 
    	(900,"CM"), (500,"D"), (400,"CD"), (100,"C"), 
    	(90,"XC"), (50, "L"), (40, "XL"), (10, "X"),
    	(9,"IX"), (5,"V"), (4, "IV"), (1, "I")
    	]

    	result = []
    	for value, symbol in digits:
    		if num == 0: 
    			break
    		if value <= num:
    			division = int(num/value)
    			num = num - value * division
    			result.append(symbol*division)

    	return "".join(result)
num = 478
res = Solution().intToRoman(num)
print("res :", res)


'''
	T(N)= O(1) 
		As there is a finite set of roman numerals, there is a hard upper  limit on how may times the loop can iterate. The upper limit is 15 times.
		and occurs for the number 3888, which is representation of MMMDCCCLXXXVIII. Therefore, we say O(1)

	S(N)= O(1)
		Amount of memory doesnt change with ths size of the input integer and is therefor constant.


	FE : number = 478

		value :  1000  - symbol :  M
		===============================
		value :  900  - symbol :  CM
		===============================
		value :  500  - symbol :  D
		===============================
		value :  400  - symbol :  CD
			value <= num. We can start cumputing
		       division :  1
		       num :  78
			   result :  ['CD']
		===============================
		value :  100  - symbol :  C
		===============================
		value :  90  - symbol :  XC
		===============================
		value :  50  - symbol :  L
			value <= num. We can start cumputing
		       division :  1
		       num :  28
			   result :  ['CD', 'L']
		===============================
		value :  40  - symbol :  XL
		===============================
		value :  10  - symbol :  X
			value <= num. We can start cumputing
		       division :  2
		       num :  8
			   result :  ['CD', 'L', 'XX']
		===============================
		value :  9  - symbol :  IX
		===============================
		value :  5  - symbol :  V
			value <= num. We can start cumputing
		       division :  1
		       num :  3
			   result :  ['CD', 'L', 'XX', 'V']
		===============================
		value :  4  - symbol :  IV
		===============================
		value :  1  - symbol :  I
			value <= num. We can start cumputing
		       division :  3
		       num :  0
			   result :  ['CD', 'L', 'XX', 'V', 'III']
		===============================
		res : CDLXXVIII

'''