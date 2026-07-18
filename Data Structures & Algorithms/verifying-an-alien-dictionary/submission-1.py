class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dt={c:i for i,c in enumerate(order)}

        for i in range(1,len(words)):
            w1=words[i-1]
            w2=words[i]

            for j in range(len(w1)):
                if j==len(w2):
                    return False
                elif dt[w1[j]]!=dt[w2[j]]:
                    if dt[w1[j]]>dt[w2[j]]:
                        return False
                    break
        return True