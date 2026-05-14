class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        cap=0
        # for i in range(l):
        #     for j in range(i,l):
        #         diff = j-i
        #         newcap = diff*min(height[i],height[j])
        #         if cap<newcap:
        #             cap = newcap
        # return cap
        i=0
        j=l-1
        flag=0
        while i<j:
            diff=j-i
            newcap = diff* min(height[j],height[i])
            if cap<newcap:
                cap=newcap
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return cap

