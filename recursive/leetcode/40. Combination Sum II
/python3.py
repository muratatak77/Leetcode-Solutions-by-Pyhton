class Solution:
    def combinationSum2(self, candidates, target):

        result = []
        candidates.sort()
        print("candidates : ", candidates)

        
        def backtracking(start, remain, slate):
            print(" remain : ", remain)
            if(remain < 0):
                return

            if(remain == 0):
                result.append(slate[:])
                print("         APPEND OUT : ", result)
                return
                
            for i in range(start, len(candidates)):
                print("     i : ", i, " - start : ", start)

                if(i==start or candidates[i-1] != candidates[i]):
                    print("remain-candidates[i] : ", remain-candidates[i])
                    if remain-candidates[i] >= 0:
                        slate.append(candidates[i])
                        print("         Slate Append : ", slate)
                        backtracking(i+1, remain-candidates[i], slate)
                        slate.pop(-1)
                        print("         Slate POP : ", slate)


        backtracking(0, target, [])
        return result
        
candidates = [2,5,2,2,1]
candidates = [10,1,2,7,6,1,5]
target = 8
# target = 5

print(Solution().combinationSum2(candidates,target))