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
