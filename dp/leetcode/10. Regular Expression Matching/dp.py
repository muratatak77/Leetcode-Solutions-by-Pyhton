'''
	First we need to understant logic :

		* : matches zero or more occurence of character before *
		. : matches any single character

		like : 
		a.b = acb , aab, axb   > True . Because we can put any single char beetween a and b
		a.b = ab, acyb > False. 

		a*b = b, ab, aab, aaab > True. Because * requires zero or more occurences matches before *.
		      which char before * : a. we can skip or we can put multiple a

		     a , acb  > False. 
		     	we need at least b for a matching. We can put any single char between a and b.


		a*b.*y = by, bly, ably, ablmy  > True .

			we can skip a or we can put multiple because there is * before a.
			b should be every time after a or as a first char. because there is "." between b and y, so b and y should be every time in matching.
			we should put a single char between b and y. 

			. = any char ,  * = zero or more occurences
			.* means zero or more occurences of any char. we can put one or multiple any char between b and y


			ay , ab > False. 

			because we need b or any single char after b.


`	We need to iterate every case for pattern and text. 

	We can apply a DP - bottom up solution in a 2D DP table. 
	as row we can put pattern , column could be text

		
		we can check every char in a DP table. 

		like  as pattern =   a * b . * y  text = bly

		  first we can check empty string in DP > True
		  
		  dp[0][0] will be True becaue empty string can match an empty string. 

		  We can seperate 2 case. First base case. second filling the inner cells case.

		  after if we reach * mark , we can back 2 steps a column and in the same row. Because * means, zero or more match
		  if we encounter . or same matching we can get dioganal item to the current cell. 
		
			exp :

					pattern				    

			    0 1 2 3 4 5 6
			      a * b . * y
 		    0   T F T F F F F
	text    1 b F F F T F T F
	`	  	2 l F F F F T T F
		  	3 y F F F F F T T


		  some cases : 

		  case 1 : 
		  	j = 4 , i : 2

		  	pattern = a*b.*
		  	text =    bly

		  	this is the match. becuase we can skip previous first star "a". we need 1 "b"  after b any single char. and after single char zero or more any chars.
			
			pattern[5] is a "." and we can get and update the current cell from 1 top cell

		   case 2: 
		   	text =    "xaabyc"
			pattern = "xa*b.c"
		   	j = 3, i : 3

		   	pattern[1] =  a
		   	text[2] = a

		   	confirm : 
		   			xa*
		   		xaa

		   		There is * means should be zero or more accurate before . like aa in the text


'''

def isMatcht(text, pattern):
	
	#we can create a dp. 
	#column would be pattern
	#row would be text
	#when we generate a dp , every time we can create first column and after rows.
	
	dp = [[0 for _ in range(len(pattern)+1)] for _ in range(len(text)+1) ]

	print("dp : ", dp)
	#empty string matchs empty string
	dp[0][0] = 1

	#base case for first row. We don't need to check first column because empty pattern and at least one char everytime will be False.
	#if we have  case like a* or a*b* we need to check previous 2 cells in this row
	for i in range(1,len(dp[0])):
		if pattern[i-1] == "*":
			dp[0][i] = dp[0][i-2]


	print("dp : ", dp)
	print("len dp : ", len(dp))
	print("len dp[0] : ", len(dp[0]))

	#inner case filling
	
	for i in range(1,len(dp)):
		for j in range(1,len(dp[0])):
			print(" i : ", i)
			print(" j : ", j)
			print("		pattern[j-1] :", pattern[j-1] )
			print("		text[i-1] :", text[i-1] )

			#if char equal . or pattern and text chars match, 
			#we can put from getting directly diagonal item to the current cell
			if pattern[j-1] == "." or pattern[j-1] == text[i-1]: 
				dp[i][j] = dp[i-1][j-1]
				print("		get from dioganal : ", dp[i][j])

			#if current pattern char equal * ,
			#we can go 2 cell back in the current row and we can put this item to the current cell
			elif pattern[j-1] == "*":
				dp[i][j] = dp[i][j-2]
				print(" 	-------------------	")
				print("			dp[i][j] : " , dp[i][j] ) 					
				print("			pattern[j-2] :", pattern[j-2] )
				print("			text[i-1] :", text[i-1] )


				#but , if we have in the previous cell a point 
				#or if we have a equal char. look case 1 above.
				if pattern[j-2] == "." or pattern[j-2] == text[i-1]:
					dp[i][j] = dp[i][j] or dp[i-1][j]
					print("				changed dp[i][j] : " , dp[i][j] ) 					
				
			print("------------------------------------------")

	last = dp[len(text)][-1]

	print("dp : ", dp)

	return last == 1

text = "bly"
pattern = "a*b.*y"


text = "xaabyc"
pattern = "xa*b.c"

text = "aa"
pattern = "a*"

res = isMatcht(text, pattern)
print("res : ", res)






'''
T(N) = O(NxM) Lenght of text and pattern
T(S) = O(NXM) 
'''
		

