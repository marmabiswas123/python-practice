class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        def margeSort(arr):
            if len(arr) <= 1:
                return arr
            
           
            mid = len(arr) // 2
            left_part = arr[:mid]
            right_part = arr[mid:]

            left_part = margeSort(left_part) 
            right_part = margeSort(right_part)

            return marge(left_part, right_part) 

        def marge(left, right):
            new = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
               
                if left[i] < right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1    
            
            new.extend(left[i:])
            new.extend(right[j:])
            return new

      
        return margeSort(nums)