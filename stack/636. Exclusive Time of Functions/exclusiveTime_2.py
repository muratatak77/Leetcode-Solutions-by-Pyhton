'''
    We can pply as mention as in the question ,we can use stack data structure to keep our process during the exucution time.

    first we can suppose function ids is a stack process. We can append or pop from stack by using function ids.
    second we have timestamp. To get difference times stamps and we can update our function ids finally.

    like this case 

    n = 2
    
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

    0:start:0

    function id = 0
    timestamp = 0
    global result array in initial will be : res = [0,0]
    stack = [function_id] so stack = [0]

    we need to a previous variable to pass times stamps variables.


    item 2 : 

        1:start:2

        getting start again but we have different function id : 1

        we can update our global result 1th item by using stack final item.

        if get start:
            if stack is not empty:
                res[stack final item] += current_time stamp  - prev time stamps
            stack.append(current time stamp)
            prev time stamp = current_time stamp

        1:end:5

        else if get end:
            res[stack_fnal_item] += current_time_stamp - prev time stamp + 1 
            stack.pop()
            prev_time_stamp = current_time_stamp - prev_time_stamp + 1
        
        return global_result


'''

from typing import List 
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0] * n
        s = logs[0].split(":")
        stack = [int(s[0])]
        prev = int(s[2])

        #we can start next item , because we processed first item 
        i = 1

        while i < len(logs):

            s = logs[i].split(":")
            if s[1] == "start":
                if stack:
                    res[stack[-1]] += int(s[2]) - prev
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                res[stack[-1]] += int(s[2]) - prev + 1
                stack.pop()
                prev = int(s[2]) + 1
            i+= 1

        return res


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
res = Solution().exclusiveTime(n, logs)
print("res : ", res)


'''
 T(N) = O(N) , N is item of length logs
 S(N) = O(N) , the stack can grow up to most n/2

 '''

