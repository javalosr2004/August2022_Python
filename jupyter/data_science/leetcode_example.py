class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) == len(nums)

example1 = Solution()

print(example1.containsDuplicate([1,2,3,1]))