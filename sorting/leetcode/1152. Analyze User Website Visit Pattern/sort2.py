from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        
        name2site = defaultdict(list)
        print("name2site : ", name2site)

        seq2names = defaultdict(set)
        print("seq2names : ", seq2names)
        
        for ts, name, site in sorted(list(zip(timestamp, username, website))):
            print("  name : ", name, " - site :", site)
            print("  name in name2site : ", name in name2site, " - name : ", name, " - name2site : ", name2site)

            if name in name2site and len(name2site[name]) >= 2:
                print("   name2site[name] : ", name2site[name])
                l = len(name2site[name])
                print("  l : ", l )
                for i in range(l):
                    for j in range(i + 1, l):
                        print("         i : ", i , " - j :", j)
                        newseq = (name2site[name][i], name2site[name][j], site)
                        print("         newseq : ", newseq)
                        seq2names[newseq].add(name)
                        print("         seq2names : ", seq2names)
                print("  =========== if end ===========")
            name2site[name].append(site)
        print("finally name2site : ", name2site)
        print("=========== for end ===========")
        
        print("finally seq2names len : ", len(seq2names))
        print("finally seq2names : ", seq2names)


        _max = 0
        res = ""
        for k,v in sorted(seq2names.items()):
            if _max < len(v):
                res = k
                _max = len(v)

        # print("res :", res)

        # res = sorted(seq2names, key = lambda e:(-len(seq2names[e]), e))[0]
        return res


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

res = Solution().mostVisitedPattern(username, timestamp, website)
print("res ; ", res)


