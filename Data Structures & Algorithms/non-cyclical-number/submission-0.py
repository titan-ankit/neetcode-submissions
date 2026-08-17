class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        number = n
        while number != 1: 
            total = 0
            while number > 0: 
                digit = number % 10
                total += digit**2
                number //= 10
            if total not in seen: 
                seen.add(total)
            elif total in seen: 
                return False
            number = total
        
        return True

