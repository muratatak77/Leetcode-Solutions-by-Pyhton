from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # I can sort in initial
        # I can walk trough all interval list
        # we need to match first pair finish time and next pair start time. If  first pair finish time grater than the secodn pair start time there is a overlapping.
        
        intervals.sort(key=lambda x:x[0])

        res = []
        res.append(intervals[0])
        for interval in intervals:
            if res[-1][1] > interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
res = Solution().merge(intervals)
print(res)
