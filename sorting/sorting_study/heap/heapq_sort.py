from heapq import heappop, heappush

def heap_sort(arr):
	heap = []
	for item in array:
		heappush(heap, item)

	ordered = []

	while heap:
		ordered.append(heappop(heap))

	return ordered

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))