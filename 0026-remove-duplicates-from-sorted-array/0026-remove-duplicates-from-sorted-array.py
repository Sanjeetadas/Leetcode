class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=1
        for traverse in range(1, len(nums)):
            if nums[traverse] != nums[traverse-1]:
                nums[start] = nums[traverse]
                start+=1
        
        return start