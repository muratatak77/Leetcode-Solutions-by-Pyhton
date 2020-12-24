import heapq
class Solution:
	def minMeetingRooms(self, intervals):
		
		# If there is no meeting to schedule then no room needs to be allocated.
		if not intervals:
			return 0

		# The heap initialization
		free_rooms = []

		# Sort the meetings in increasing order of their start time.
		intervals.sort(key= lambda x: x[0])
		print("intervals : ", intervals)

		# Add the first meeting. We have to give a new room to the first meeting.
		heapq.heappush(free_rooms, intervals[0][1])
		print("first heapq.heappush : ", free_rooms)

		# For all the remaining meeting rooms
		for i in intervals[1:]:
			print("i :::", i)
			# If the room due to free up the earliest is free, assign that room to this meeting.
			print("free_rooms[0] <= i[0]  : ", free_rooms[0] ,"<= ", i[0])
			if free_rooms[0] <= i[0]:
				heapq.heappop(free_rooms)
				print("heapq.heappop(free_rooms) : ", free_rooms)

			# If a new room is to be assigned, then also we add to the heap,
			# If an old room is allocated, then also we have to add to the heap with updated end time.
			heapq.heappush(free_rooms, i[1])
			print("heapq.heappush ;" , free_rooms)
			print("============")

		# The size of the heap tells us the minimum rooms required for all the meetings.
		return len(free_rooms)



a = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
res = Solution().minMeetingRooms(a)
print(res)