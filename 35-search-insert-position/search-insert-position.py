class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        else:
            nums.append(target)
            nums.sort()
            b=nums.index(target)
            return b
  