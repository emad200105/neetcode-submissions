class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5=0
        cnt10=0

        for bill in bills:
            if bill==5:
                cnt5+=1
            elif bill==10:
                if cnt5:
                    cnt10+=1
                    cnt5-=1
                else:
                    return False
            else:
                if cnt5 and cnt10:
                    cnt5-=1
                    cnt10-=1
                elif cnt5>2:
                    cnt5-=3
                else:
                    return False
        return True