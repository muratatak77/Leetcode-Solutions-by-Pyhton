class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        print("flightMap :", self.flightMap)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        print("after reverse sorting flightMap :", self.flightMap)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        print("    origin : ", origin)
        destList = self.flightMap[origin]
        print("    destList : ", destList)
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            print("         nextDest : ", nextDest)
            self.DFS(nextDest)
        self.result.append(origin)
        print("result : ", self.result)


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

res = Solution().findItinerary(tickets)
print("res : ", res)
