class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1


        digits.reverse()


        for i in range(len(digits)):
            if (digits[i] + carry) < 10:
                digits[i] = digits[i] + carry
                carry = 0
            else:
                digits[i] = 0


        digits.reverse()
        if digits[0] == 0:
            digits.insert(0,1)  


        return digits
