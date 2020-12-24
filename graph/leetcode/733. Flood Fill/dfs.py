class Solution:
	def floodFill(self, image, sr, sc, newColor):

		oldcolor = image[sr][sc]
		if oldcolor == newColor: return image
		
		def getneighbors(x,y):
			result = []
			if x+1 <= len(image)-1:
				result.append((x+1,y))

			if y+1 <= len(image[0])-1:
				result.append((x, y+1))

			if x-1 >= 0:
				result.append((x-1, y))

			if y-1 >= 0:
				result.append((x, y-1))

			return result

		def dfs(x,y):
			image[x][y] = newColor
			neighbors = getneighbors(x,y)
			for row,col in neighbors:
				if image[row][col] == oldcolor:
					dfs(row, col)

		dfs(sr,sc)
		return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2


# image =[[0,0,0],[0,1,1]]
# sr =1
# sc =1
# newColor = 1


ans = Solution().floodFill(image, sr, sc, newColor)
print(ans)
