class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(num)):
            first=num[i] #2
            sec = target-first 
            if sec in m:
                return [m[sec], i]
            m[num[i]]=i