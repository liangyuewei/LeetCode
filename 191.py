class Solution(object):
    def hammingWeight01(self, n):
        srt = 0
        mark = 1
        for i in range(32):
            if n & mark:
                srt += 1
            mark = mark << 1
        return srt

    def hammingWeight02(self, n):
        srt = 0
        while n != 0:
            srt += 1
            n = n & (n -1)
        return srt