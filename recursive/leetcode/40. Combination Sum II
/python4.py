'''
    We can apply backtracking approach for this problem.
    like our case 
        candidates = [10,1,2,7,6,1,5]
        we can sort candidates 
        
        cand = [1,1,2,5,6,7,10]

        our target = 8
                    
                    [1,1,2,5,6,7,10]

   s = 1. i=1                       1 

s = 2 i=2                      1,1   

s = 3 i=3       1,1      1,1,2   1,1,5   1,1,6

1,1,2,5

i=4, s=3
i=5, s=3

i should be equal s , or previous item shouldn't be equal next item because we don't want to repeated results.



(we got totaly > target. 
we don't need to call recursive function.)


we can call each recursive call inside the for loop.
    

    #base case, leaf nodes
    we can define a remain that has been calls remain = remain - candidates[i]

    if this remain < 0 
        return 

    if this remain == 0
        result.append(slate)
        

'''
class Solution:
    def combinationSum2(self, candidates, target):
        
        result = []
        candidates.sort()

        def helper(start, remain, slate):

            #base case
            if remain < 0:
                return
            if remain == 0:
                result.append(slate[:])


            #recursive case
            for i in range(start,len(candidates)):
                if candidates[i-1] != candidates[i] or i == start:
                    if remain - candidates[i] >= 0:
                        slate.append(candidates[i])
                        helper(i+1, remain-candidates[i], slate)
                        slate.pop()

        helper(0, target, [])
        return result
        
candidates = [2,5,2,2,1]
candidates = [10,1,2,7,6,1,5]
target = 8
# target = 5

print(Solution().combinationSum2(candidates,target))
