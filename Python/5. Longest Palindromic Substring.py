class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check_for_palindrome(s):
            return s == s[::-1]

        
        if check_for_palindrome(s):
            return s
        
        substring_length = len(s) - 1
        while substring_length > 0:
            i = 0
            while substring_length + i <= len(s):
                substring = s[i:substring_length + i]
                if check_for_palindrome(substring):
                    return substring
                i += 1

            substring_length -= 1
        
        return ''
