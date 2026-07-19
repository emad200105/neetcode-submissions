class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt=defaultdict(list)

        for st in strs:
            cnt=[0]*26
            for s in st:
                cnt[ord(s)-ord('a')]+=1
            key=tuple(cnt)
            dt[key].append(st)
        
        return list(dt.values())