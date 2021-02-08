from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        # intervals.sort()
        print("after sort 2 intervals : ", intervals)


        merged = []
        for interval in intervals:
            print("interval : ", interval)
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            # if not merged:
                # print("merged[-1][1] : " , merged[-1][1])
            print("merged : ", merged)     

            if merged: 
                print("merged[-1] : ", merged[-1])
                print("merged[-1][1] : ",merged[-1][1])

            if not merged or merged[-1][1] < interval[0]:

                print("Just append : ", interval)
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
                print("merged : ", merged)
            print("========================")


        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,9],[2,5],[19,20],[10,11],[10,13],[12,20],[0,3],[0,1],[0,2]]


res = Solution().merge(intervals)
print(res)