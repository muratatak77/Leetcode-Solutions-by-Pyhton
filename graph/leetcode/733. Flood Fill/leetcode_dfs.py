class Solution:
	def floodFill(self, image, sr, sc, newColor):

		color = image[sr][sc]
		print("color : ", color)
		print("newColor : ", newColor)

		if color == newColor: return image
		
		R = len(image) 
		print("R len : " , R)
		C = len(image[0])
		print("C len : " , C)

		def dfs(r,c):

			if image[r][c] == color:
				image[r][c] = newColor
				print("image[r][c] : ", image[r][c], " , r : ", r , " - c : ", c)
				
				if r >= 1:
					print("Call r >= 1 / c : " , c , " - r : ", r)
					dfs(r-1,c)

				if r+1 < R :
					print("Call r+1 < R / c : " , c , " - r : ", r)
					dfs(r+1,c)

				if c >= 1: 
					print("Call c >= 1 / c : " , c , " - r : ", r)
					dfs(r, c-1)

				if c+1 < C:
					print("Call c+1 < C / c : " , c , " - r : ", r)
					dfs(r, c+1)


		dfs(sr,sc)
		return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2


image =[[0,0,0],[0,2,2]]
sr =1
sc =1
newColor = 2

ans = Solution().floodFill(image, sr, sc, newColor)
print(ans)