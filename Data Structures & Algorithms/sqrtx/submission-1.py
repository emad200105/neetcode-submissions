class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low,high=0,x//2

        while low<=high:
            mid=(low+high)//2
            res=mid*mid
            if res==x:
                return mid
            elif res>x:
                high=mid-1
            else:
                low=mid+1
        return high