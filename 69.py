# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2

class  Solution(object):
    def mysqrt(self, n):
        if (n == 0) or (n == 1): return n
        left, right = 0, n
        res = 0
        while left <= right:
            mid = (left + right) / 2
            if mid == n / mid:
                return mid
            elif mid > n / mid:
                left = mid - 1
            else:
                right = mid + 1
                res = mid
        return res
