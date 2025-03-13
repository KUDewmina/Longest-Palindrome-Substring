class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = set()
        max_lenght = 0
        longest_element = ''
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                sub_string = s[i:j]
                if sub_string == sub_string[::-1] :
                    palindromes.add(sub_string)
        for element in palindromes:
            if len(element) > max_lenght:
                max_lenght = len(element)
                longest_element = element
        return longest_element
