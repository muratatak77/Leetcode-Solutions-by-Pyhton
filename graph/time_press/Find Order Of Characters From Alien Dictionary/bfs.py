import collections

def alienOrder(words):

    pre = collections.defaultdict(set)
    suc = collections.defaultdict(set)

    print("pre : ", pre)
    print("suc : ", suc)

    for pair in zip(words, words[1:]):
        print("pair : ", pair)

        for a, b in zip(*pair):
            print("a : ", a)
            print("b : ", b)
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
                print("suc :", suc)
                print("pre :", pre)
                break
    print("suc :", suc)
    print("pre : ", pre)

    chars = set(''.join(words))
    print("chars : " , chars)

    charToProcess = chars - set(pre)
    print("charToProcess : ", charToProcess)
    order = ''
    while charToProcess:
        ch = charToProcess.pop()
        order += ch
        for b in suc[ch]:
            pre[b].discard(ch)
            if not pre[b]:
                charToProcess.add(b)
    return order * (set(order) == chars)


words = ["baa", "abcd", "abca", "cab", "cad"]
alienOrder(words)