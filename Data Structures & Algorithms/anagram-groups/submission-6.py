class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt=dict()

        for sts in strs:
            cnt=[0]*26
            
            for chr in sts:
                cnt[ord(chr)-ord('a')]+=1

            key=tuple(cnt)
            if key in dt:
                dt[key].append(sts)
            else:
                dt[key]=[sts]

        return list(dt.values())