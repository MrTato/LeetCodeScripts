class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        result = 0
        while result <= n:
            result = 3**x
            if result == n:
                return True
            x += 1
        return False
