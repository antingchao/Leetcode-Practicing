# https://leetcode.com/problems/first-missing-positive/description/
# 41. First Missing Positive
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# reference: https://leetcode.com/problems/first-missing-positive/solutions/5694826/video-use-index-to-count-numbers/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0] # keep the positive nums
        nums.sort() # if 1~N exist, value of nums[i] should be i+1
        tar = 1 # first missing positive num
        for num in nums:
            if num > tar: # missing tar
                return tar
            elif num == tar:
                tar += 1
            # elif num < tar: # e.g. nums = [1, 2, 2, 3, ...], the second 2 will derived to this situation
                # next
        return tar