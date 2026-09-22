class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # without using sets
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True
        return False