from collections import Counter

def minWindow(s, t):
	print("S : ", s, " - T: ", t)
	if not s or not t:
		return ""

	dict_t = Counter(t) # dictinoary which keeps a count of all the unique chars in t
	print("dict_t :", dict_t)

	required = len(dict_t) #  number of uniq chars
	print("required :", required)

	l,r = 0,0

	formed = 0 #track of how many unique chars in t are present in the current window in the desired frequency

	window_counts = {} # keeps a count of all unique chars in the current window
	print("window_counts : ", window_counts) 

	# ans = window_len, left, right
	ans = [float("inf"), None, None]
	print("ans : ", ans) 

	while r < len(s):
		print(" >>>> start R : ", r, " L : ", l)
		character = s[r] # A
		print("character : ", character)

		window_counts[character] = window_counts.get(character, 0)+1 
		print("window_counts : ", window_counts)

		print("window_counts[character] : ", window_counts[character])
		print("dict_t[character] : ", dict_t[character])

		#if frequency of the current character added equals to the desired count in t then increment the formet count by 1
		if character in dict_t and window_counts[character] == dict_t[character]:
			formed += 1
			print("formed increment : ", formed)


		while l <= r and formed == required:
			print("start formed == required ----- R: ", r , " - L :" , l)
			character = s[l]
			print("character : ", character)
			#save the smallest window
			if r-l+1 < ans[0]:
				ans = (r-l+1,l,r)
				print("ANS : ", ans)

			window_counts[character] -= 1 #no longer part of the window 
			print("window_counts[character] - 1 : ", window_counts[character] ,  " - window_counts : ", window_counts)
			if character in dict_t and window_counts[character] < dict_t[character]:
				formed -= 1
				print("formed decrease - 1 : formed: ", formed)

			l+=1 #move left pointer ahead, this would help to look for a new window
			print("--------------")

		r += 1
		print("----------------------------")

	if ans[0] == float("inf"):
		return ""
	else:
		return s[ans[1]:ans[2]+1]

S = "ADOBECODEBANC"

S = "AEBANC"
T = "AB"
res = minWindow(S,T)
print("RES : ", res)



