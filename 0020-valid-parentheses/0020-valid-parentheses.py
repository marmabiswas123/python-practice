class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        stack=[]
        pair={'(':')','{':'}','[':']'}
        for x in s:
            if x =='(' or x=='{' or x=='[':
                stack.append(x)
            elif len(stack)==0:
                return False
            elif x != pair[stack.pop()]:
                return False
        if len(stack)>0:
            return False
        return True
