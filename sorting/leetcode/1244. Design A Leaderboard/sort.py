from collections import defaultdict
import heapq

class Leaderboard(object):

    def __init__(self):
        self.hmap = defaultdict(int)
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.hmap[playerId] += score 
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        sort_list = sorted(self.hmap.items(),  reverse= True, key=lambda item: item[1])
        sum = 0
        for k,v in sort_list[:K]:
            sum += v
        return sum

        # for k,v in sorted(self.hmap.items(), key=lambda item: item[1]):
            # print(v)

        # self.hmap.sort(key=lambda x: x.values())

        # return sum(heapq.nlargest(K, self.hmap.values()))
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.hmap[playerId]
        


# Your Leaderboard object will be instantiated and called as such:

# ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
# [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

obj = Leaderboard()
obj.addScore(1,73)
obj.addScore(2,12)
obj.addScore(3,39)
obj.addScore(4,51)
obj.addScore(5,4)

param_2 = obj.top(3)
print(param_2)
obj.reset(1)