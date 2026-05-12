class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for digit in digits:
            s+= str(digit)
        nums = str(int(s) + 1)
        result=[]
        for num in nums:
            result.append(int(num))
        return result        