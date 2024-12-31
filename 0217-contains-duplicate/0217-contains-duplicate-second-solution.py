class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        #nums = [1,2,3,4]
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
