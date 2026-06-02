class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 1
        for i in range(len(digits)):
            sum += (10 ** (len(digits) - (i + 1)))*(digits[i])
        digit_array = []
        for digit in str(sum):
            digit_array.append(int(digit))
        return digit_array