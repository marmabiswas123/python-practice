class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        # count={}
        # for num in nums:
        #     if num in count:
        #         count[num]+=1
        #     else:
        #         count[num]=1
        #     if count[num]>len(nums)//2:
        #         return num
        count =0
        candidate=0
        for i in nums:
            if count == 0 :
                candidate=i
            if candidate == i:
                count+=1
            else:
                count -=1
        return candidate