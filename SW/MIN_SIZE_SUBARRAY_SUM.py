class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0

        mini=1000

        while r<len(nums):
            if sum(nums[l:r+1])<target:
                r+=1
            else:
                mini=min(mini,r-l+1)
                l+=1
            
        if mini==1000:
            return 0
        return mini
