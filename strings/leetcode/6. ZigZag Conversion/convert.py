'''
	we can think this way: 
		numrows will be our base structer size.

		we can keep an output array : 
			
			output = [""] * numrows
			
			means output will be = ["","",""]

			and we can fill up in this array by using iterative

			our structer like : 

			s = "PAYPALISHIRING", numRows = 3

			line 0 = P     A      H      N
			-------------------------------
			line 1 = A  P  L  S   I   I  G
			-------------------------------
			line 2 = Y     I      R


			we can increment from 0 to 2 the 'line'. When we reach line 2 means = (numrows - 1)  we can decrease line and line param can go to line 1.

			output[line(0)] += s[0]
			output[line(1)] += s[1]
			output[line(2)] += s[2]

			output = ["P","A","Y"]

			and 

			output[line(1)] += s[3]
			output = ["P","AP","Y"]

			and we reach again line 0
							
			output[line(0)] += s[4]

			output = ["PA","AP","Y"]

			so on...

			But numrows is 1 we don't need go to back up and dpwn line variable. 


'''

class Solution:
	def convert(self, s: str, numRows: int) -> str:

		if not s:
			return ""
		
		if len(s) == 0:
			return ""

		line = 0
		pre_line = 1
		output = [""] * numRows

		for i in range(len(s)):
			output[line] += s[i]

			if numRows > 1:
				line += pre_line
				#already reach up or down we can extract the line from pre_line so we can multiple -1
				if line == 0 or line == numRows -1:
					pre_line *= -1

		return "".join(output)


s = "PAYPALISHIRING"
numRows = 3
res = Solution().convert(s, numRows)
print("res : " , res)