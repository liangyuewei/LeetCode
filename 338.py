class Solution(object):
    def countbits(self, num):
        result = [0, 1]
        while len(result) < num + 1:
            result += [ x + 1 for x in result]
        return result[:num + 1]