class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        answer = []
        for num in nums:
            answer.append(rank[num])
        return answer