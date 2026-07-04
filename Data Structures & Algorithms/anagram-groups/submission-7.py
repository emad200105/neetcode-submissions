class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt=dict()

        for st in strs:
            cnt=[0]*26

            for s in st:
                cnt[ord(s)-ord('a')]+=1
            
            key=tuple(cnt)
            if key in dt:
                dt[key].append(st)
            else:
                dt[key]=[st]
        
        res=[]
        for key in dt:
            res.append(dt[key])
        return res