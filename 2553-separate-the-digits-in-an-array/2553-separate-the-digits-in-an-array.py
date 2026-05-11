class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits=[]
        for num in nums:
            dig_num=[]
            while num>0:
                dig_num.append(num%10)
                num=num//10
            digits.extend(dig_num[::-1])
        return digits