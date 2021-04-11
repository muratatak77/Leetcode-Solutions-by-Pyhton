from typing import List 
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        res = [0] * n

        s = logs[0].split(":")
        stack.append(int(s[0]))
        i = 1
        prev = int(s[2])

        print("res : ",res)
        print("stack : ", stack)
        print("prev : ", prev)
        print("-------------------")

        while i < len(logs):
        	s = logs[i].split(":")
        	print("	s : ", s, " - i :", i)
        	print("		prev :", prev)

        	if s[1] == "start":
        		if stack:
        			res[stack[-1]] += int(s[2]) - prev
        			print("		res changed start. int(s[2]) - prev : ", res)
        		stack.append(int(s[0]))
        		print("		stack changed : ", stack)
        		prev = int(s[2])
        	else:
        		res[stack[-1]] += int(s[2]) - prev + 1
        		print("		res changed end.+= int(s[2]) - prev + 1 : ", res)
        		stack.pop()
        		print("		stack pop : ", stack)
        		prev = int(s[2]) + 1
        	i+=1 
        	print("---------------------------")

        return res


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
res = Solution().exclusiveTime(n, logs)
print("res : ", res)


'''
public class Solution {
    public int[] exclusiveTime(int n, List < String > logs) {
        Stack < Integer > stack = new Stack < > ();
        int[] res = new int[n];
        String[] s = logs.get(0).split(":");
        stack.push(Integer.parseInt(s[0]));
        int i = 1, prev = Integer.parseInt(s[2]);
        while (i < logs.size()) {
            s = logs.get(i).split(":");
            if (s[1].equals("start")) {
                if (!stack.isEmpty())
                    res[stack.peek()] += Integer.parseInt(s[2]) - prev;
                stack.push(Integer.parseInt(s[0]));
                prev = Integer.parseInt(s[2]);
            } else {
                res[stack.peek()] += Integer.parseInt(s[2]) - prev + 1;
                stack.pop();
                prev = Integer.parseInt(s[2]) + 1;
            }
            i++;
        }
        return res;
    }
}


'''