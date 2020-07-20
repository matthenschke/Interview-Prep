# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums) -> int:
        def segregate(nums):
            j = 0
            for i in range(len(nums)):
                if nums[i] <= 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            return j

        def findMissing(nums):
            n = len(nums)
            for i in range(n):
                if abs(nums[i]) - 1 < n and nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

            for j in range(n):
                if nums[j] > 0:
                    return j + 1

            return n + 1

        start = segregate(nums)
        return findMissing(nums[start::])
