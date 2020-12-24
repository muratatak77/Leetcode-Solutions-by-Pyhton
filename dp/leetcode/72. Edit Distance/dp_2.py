'''
	Main logic is substring between 2 strings for each char.
	We will convert st1 to st2 by the min number operation. 
		like : 
		
		S1 = "adceg"
		S2 = "abcfg"

		for example we can get some substring :

			S1[0:3] = adc
			S2[0:3] = abc 
	
			Match case :
				we have 2 same character. We can do nothing by the same char. like "c". 
			

			Replacement case 

				S1[0:2] = ad
				S2[0:2] = ab

				we should replace b : d. we have 1 operation min.

			Insertion case

				S1[0:2] = ad
				S2[0:2] = abc

				we have totaly 2 case in this convertion. 1 :  (d>b) replace  2 : _ > c insert

			
			Removing case:

				S1[0:2] = ad
				S2[0:1] = a

				we can remove "d" and we have 1 remove operation


		We can match all substring but will be take long time.
		We can apply an 2D array DP solution.
			first word represent rows , and second represents cols.
			we will try to convert rows > cols 
			and we have 3 cases 

				Remove will be bottom > up arraw
				Insert will be left > right arraw
				Replace will be diagonal arraw
				

				We can generate a 2d array rows : len(w1) + 1 . cols : len(w2)+1
				
				we will iterate 2 loops row and columns
					if we have match we copy just from diagonal case  min total number
					else
						we set to the current cell by compute min(remove, insert, replace) + 1


'''

def minDistance(word1, word2):

	w1Size = len(word1)
	w2Size = len(word2)

	print("w1Size : ", w1Size)
	print("w2Size : ", w2Size)

	#dp table
	#0 meaning is there is no any operation. Null string
	table = [[0 for _ in range(1+w2Size)] for _ in range(1+w1Size)]

	#base cases
	#filling first row
	for col in range(1,1+w2Size):
		table[0][col] = col

	#filling first col
	for row in range(1,1+w1Size):
		table[row][0] = row

	#internal traversel cases
	for row in range(1,1+w1Size):
		for col in range(1,1+w2Size):
			if word1[row-1]==word2[col-1]:
				table[row][col] = table[row-1][col-1]
			else:
				table[row][col] = min(table[row][col-1], table[row-1][col-1], table[row-1][col])+1

	print("table : ", table)

	return table[-1][-1]



word1 = "horse"
word2 = "ros"

word1 = "adceg"
word2 = "abcfg"

ans = minDistance(word1, word2)
print(ans)


'''
	T(N) = T(row*col) = T(mn)
	S(N) = T(mn)
'''