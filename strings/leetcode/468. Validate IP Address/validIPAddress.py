class Solution:
	def validIPAddress(self, IP: str) -> str:


		def validate_IPV4():
			nums = IP.split(".")
			for x in nums:
				#length of chuck between 1 and 3
				if len(x) == 0 or len(x) > 3:
					return "Neither"

				#no extra leading zero
				if x[0] == '0' and len(x) != 1:
					return "Neither"

				#only digits are allowed
				#Validate integer 0 - 255
				if not x.isdigit() or int(x) > 255:
					return "Neither"

			return "IPV4"

		
		def validate_IPV6():
			nums = IP.split(":")
			hexdigits = "0123456789abcdefABCDEF"

			for x in nums:
				#1 .at least one and not more than 4 hexdigits in one chunk
				if len(x) == 0 or len(x) > 4:
					return "Neither"

				#check in hexdigits
				for c in x:
					if c not in hexdigits:
						return "Neither"

			return "IPV6"


		if IP.count('.') == 3:
			return validate_IPV4()

		elif IP.count(':') == 7:
			return validate_IPV6()
		else:
			return "Neither"


IP = "172.16.254.1"
IP = "1e1.4.5.6"
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
# IP = "256.256.256.256"

res = Solution().validIPAddress(IP)
print("res : ", res)



'''
	T(N) = O(N) 
	S(N) = O(1)
	
'''