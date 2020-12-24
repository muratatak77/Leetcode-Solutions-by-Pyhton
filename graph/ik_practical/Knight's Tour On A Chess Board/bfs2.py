# Complete the function below.
import collections

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
	# Write your code here.
	
	DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
	
	def getNeighbors(r,c):
		neighbors = []
		for dr, dc in DIRECTIONS:
			new_r, new_c = r + dr, c + dc
			if 0 <= new_r < rows and 0 <= new_c < cols:
				neighbors.append((new_r, new_c))
	
		return neighbors
	
	start_cell = start_row, start_col
	q = collections.deque()
	q.append((start_cell, 0))
	visited = {start_cell}
	
	while q:
		cell, count = q.popleft()
		if cell == (end_row, end_col):
			return count
			
		neighbors = getNeighbors(*cell)
		for new_cell in neighbors:
			if new_cell not in visited:
				q.append((new_cell, count + 1))
				visited.add(new_cell)
	return -1