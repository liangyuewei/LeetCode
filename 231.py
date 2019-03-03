## 2的幂次方问题

class Solution(object):
    def isPowerofTwo(self, n):
        return n > 0 and not n & (n - 1)