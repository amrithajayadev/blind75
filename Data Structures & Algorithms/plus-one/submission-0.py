class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            digits[i] += carry
            carry = digits[i]//10
            digits[i] = digits[i]%10

        if digits[0] == 0:
            return [1]+digits
        else:
            return digits