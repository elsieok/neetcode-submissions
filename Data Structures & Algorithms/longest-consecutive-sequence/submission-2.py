class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        nums_set = set(nums)

        for num in nums_set:
            curr_cnt = 1
            if num - 1 not in nums_set:
                i = 1
                while num + i in nums_set:
                    curr_cnt += 1
                    i += 1
                res = max(res, curr_cnt)

        return res

