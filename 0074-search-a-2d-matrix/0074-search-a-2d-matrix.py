class Solution:
     def bsearch(self, arr, start, end, target):
        if start>end:
            return False
        if arr[start] == target:
            return True
        if arr[end] == target:
            return True
        mid = start + ((end-start)//2)
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            return self.bsearch(arr,mid+1,end,target)
        elif arr[mid]>target:
            return self.bsearch(arr,start,mid-1,target)
        else:
            return False
     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1 and len(matrix[0])==1:
            if matrix[0][0]!=target:
                return False
            else: 
                return True
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            if target<matrix[i][0]:
                return False
            if target>matrix[row-1][col-1]:
                return False
            if (matrix[i][0]<=target and matrix[i][col-1]>=target):
                if matrix[i][0]==target:
                    return True
                elif matrix[i][col-1]==target:
                    return True
                else:
                    return self.bsearch(matrix[i],1,col-2,target)
   