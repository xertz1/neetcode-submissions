class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = s.lower()
        filtered = re.sub(r"[^a-z0-9]" ,"",filtered)

        left = 0
        right = len(filtered) - 1

        while left < right: 
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        
        return True

        