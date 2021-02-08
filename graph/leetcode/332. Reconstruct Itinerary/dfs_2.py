#
#https://www.youtube.com/watch?v=WYqsg5dziaQ&ab_channel=TECHDOSE
#
class Solution(object):
    def findItinerary(self, tickets):

        '''
            this is a graph problem : 
                given a pairs data
                reconstract the array

            We need a adjancy list in a directed graph - dict 

            smallest lexical order sorting  
                and we can sort itineary list because sometimes we might have multiple dest  - sorting we need reverse sorting because we will use a array for result
            
            We can apply Eulerian Path algorithm
                Start and finished vertex should be same
                Postorder - DFS 

                 - starting JFK vertex , we keep following unused edges until we get stuck at certain vertex where we have no more unvisited edges
                 - We can backtrack to the previoues neighbor vertex and we can add the global result current vertex - node

        '''

        from collections import defaultdict

        # adjanceny list
        self.flightMap = defaultdict(list)

        #fill flightMap
        for ticket in tickets:
            src, dst = ticket[0], ticket[1]
            self.flightMap[src].append(dst)

        # sorting lexical order
        # we can do it reverse=True because we will use to get first smallest item in DFS
        for des, iten in self.flightMap.items():
            iten.sort(reverse=True)

        #global result
        self.result = []
        self.DFS('JFK')
        return self.result[::-1]

    #Eulerian Path Alg - Postorder DFS
    #JFK : [SFO, ATL]
    #ATL : [SJC]
    #
    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

res = Solution().findItinerary(tickets)
print("res : ", res)


'''
Time Complexity :
     
     V  : Number of vertex
     E  : Number of edges

     We have sorting : N LogN

     What is the N in this directed graph ?

         N = E/2 in worst case. Graph is not balanced. Connections are concentered in a single airport.
         JFK might have half of the flights (since we still need the rturn flight)
                    
                    LGB
                    .
                    | |
                    | |
                      .
         SJC <----- JFK -----> SFO
             ------>   <-----
    

     N = E/2.V in avarage case. Each node has the equal number of outgoing flights.

        JFK ---> SJC ---> SFO -----> LGB

        we have total complexity : |V| (NLogN) = N = E/2V  > O(E/2V log E/2V) > O(E log E/V)

Space : 
    |V| is number of vertex  : Airports
    |E| us number if edges  : Flights 
    (V+E)



     


'''