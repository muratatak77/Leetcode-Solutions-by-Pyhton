import heapq

class Solution(object):
	def minMeetingRooms(self, intervals):
		
		#we need to sort increasingly start time, in hea-min approach
		intervals.sort(key = lambda x: x[0])
		
		#we can use min-heap in this problem.
		free_rooms = []

		#we can build a min-heap first ending times of meeting. 
		heapq.heappush(free_rooms, intervals[0][1])

		#we gonna walk trough for every each meeting record , we ll check current meeting ending time and next meeting start time. 
		#if the ending time is grater than the next meeting starting time we need extra 1 more room for next meeting. 
		#when a room is free we can use for next meeting room istead of free room
		
		#for all the remaining meeting rooms
		for interval in intervals[1:]:

			#if the room due to free up the earliest is free, assign that room to this meeting
			if free_rooms[0] <= interval[0]:
				heapq.heappop(free_rooms)

			heapq.heappush(free_rooms, interval[1])


		#the size of the heap tells us the min rooms required for all the meetings
		return len(free_rooms)


a = [[1, 10], [2, 7], [3, 19]]
res = Solution().minMeetingRooms(a)
print(res)

