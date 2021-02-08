class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        '''
        we generate a graph. Every edge would be a vertex. 
        we can get an adj list set from zip(str1,str)
        
        str1 = " a a b c c ", 
        str2 = " c c d e e"
        Graph : 
        
        a ---- > c -----> e
        b -----> d
        
        in this case , our adj list : 
        a : {c}
        c : {e}
        b : {d}
        
        Genareta a graph
        and we can check constraint :  just english  letter so we can have max 26 chars
        we can count uniqu adj list size . if this size grater than 26 return false
        
        '''
        
        if str1 == str2:
            return True
        
        if len(str1) != len(str2):
            return False
        
        graph = defaultdict(set)
        unique = {}
        
        for s1,s2 in zip(str1, str2):
            graph[s1].add(s2)
            # we will check unique size after
            if s2 not in unique:
                unique[s2] = True
        
        # for check letter length
        if len(unique.keys()) >= 26:
            return False
    
        #if we have in graph multiple value depend a key, we can't convert str1 into str2  
        for neighbors in graph.values():
            if len(neighbors) > 1:
                return False
        
        return True
    
    '''
        N : len of strings
        Time and space : O(N)
        
    
    '''