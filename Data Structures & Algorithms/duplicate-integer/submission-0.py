class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums[:])):
            dupe = (True)
            non = (False)
            j = i
            while j>0 and nums[j - 1] == nums [j]:
                if nums[j - 1] == nums[j]:
                    return dupe
                else:
                    return non
        return False