class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums or len(nums) == 0: return 0 
    
        dp =  [0 for _ in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

        
