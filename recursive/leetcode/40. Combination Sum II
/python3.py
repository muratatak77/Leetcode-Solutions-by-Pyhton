class Solution:
    def combinationSum2(self, candidates, target):
        out = []
        candidates.sort()
        self.backtracking(0, candidates, target, [], out)
        return out
        
        
        
        
    def backtracking(self, start, candidates, tar, result, out):
        if(tar < 0):
            return
        if(tar == 0):
            out.append(result.copy())
            return
            
        for i in range(start, len(candidates)):
            if(i==start or candidates[i-1] != candidates[i]):
                result.append(candidates[i])
                self.backtracking(i+1, candidates, tar-candidates[i], result, out)
                result.pop(-1)

candidates = [2,5,2,1,2]
target = 5

print(Solution().combinationSum2(candidates,target))