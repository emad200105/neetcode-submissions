class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5,cnt10,cnt20=0,0,0

        for bill in bills:
            if bill==5:
                cnt5+=1
            elif bill==10:
                cnt10+=1
                if cnt5:
                    cnt5-=1
                else:
                    return False
            else:
                cnt20+=1
                if cnt10 and cnt5:
                    cnt5-=1
                    cnt10-=1
                elif cnt5>=3:
                    cnt5-=3
                else:
                    return False
        return True