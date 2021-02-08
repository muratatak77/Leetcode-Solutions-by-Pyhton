import collections

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):


		#build tree
		# grid = [ [0] * end_col for i in range(end_row) ]
		grid = [[-1 for x in range(rows)] for y in range(cols)] 
		# print(grid)
		# grid = [[],[]]
		# for x in range(rows):
		# 	for y in range(cols):
		# 		grid[x][y] = -1
		
		DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

		def getNeighbors(r, c):
			neighbors = []
			for dr, dc in DIRECTIONS:
				new_r, new_c = r + dr, c + dc
				if 0 <= new_r < rows and 0 <= new_c < cols:
					neighbors.append((new_r, new_c))

			return neighbors
			

		# def getNeighbors(x,y):
		# 	result  = []
		# 	if x+1 < rows and y+2 < cols:
		# 		result.append((x+1,  y+2))

		# 	if y+1 < cols and x+2 < rows:
		# 		result.append((x+2, y+1))

		# 	if x-1 >= 0 and y+2 <= cols: 
		# 		result.append((x-1,y+2))

		# 	if y-2 >= 0 and x+1 <= rows:
		# 		result.append((x+1,y-2))
		# 	return result




		start_cell = start_row, start_col
		print("start_cell : ", start_cell)

		q = collections.deque()
		q.append((start_cell, 0))
		print("q : ", q)

		visited = {start_cell}
		print("visited : ", visited)

		while q:
			cell, count = q.popleft() 
			print(">>> While start >>>> ")
			print("popleft cell : ", cell)
			print("popleft count : ", count)

			if cell == (end_row, end_col):
				return count

			# (curr_x,curr_y) = q.popleft()
			neighbors = getNeighbors(*cell)
			print("neighbors : ", neighbors)
			for new_cell in neighbors:
				print("new_cell : ", new_cell)
				if new_cell not in visited:

					q.append((new_cell, count + 1))
					print("Finally Q : ", q)
					visited.add(new_cell)
					print("Finally visited : ", visited)
					print("===== IF END =====")
			print("===== FOR END =====")


		return -1
	

rows = 5
cols = 5
start_row = 0
start_col = 0
end_row = 4
end_col = 1
ans  = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)
print(ans)