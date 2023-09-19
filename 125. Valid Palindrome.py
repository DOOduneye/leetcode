# Problem 125
# Easy — Two Pointer
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true *if it is a palindrome, or* false *otherwise*.
# Input: s = "A man, a plan, a canal: Panama"

# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution: 
    # O(n)
    def isPalindromePythonic(self, s: str) -> bool:
        if s == '':
            return True

        s_stripped = ""
        for i in s:
            if i.isalnum() and i != " ":
                s_stripped += i.lower()

        return s_stripped == s_stripped[::-1]

    # O(n)
    def isPalindrome(self, s: str) -> bool:
        s_stripped = ""
        for i in s:
            if i.isalnum() and i != " ":
                s_stripped += i.lower()
    
        i = 0
        j = len(s_stripped) - 1
        
        while i < len(s_stripped):
            if s_stripped[i] != s_stripped[j]:
                return False
            
            i+=1
            j-=1
        
        return True



    # O(n)
    def isPalindromeOptimal(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


