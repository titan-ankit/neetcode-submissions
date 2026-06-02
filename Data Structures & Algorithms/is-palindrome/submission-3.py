class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                new_str += s[i].lower()

        original_str_clean = ""
        for i in range(0,len(s)):
            if s[i].isalnum():
                original_str_clean += s[i].lower()
        return original_str_clean == new_str