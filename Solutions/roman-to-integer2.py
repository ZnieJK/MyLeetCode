class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i, n in enumerate(s[:-1]):
            if n == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                total -= roman_to_int[n]
            elif n == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                total -= roman_to_int[n]
            elif n == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                total -= roman_to_int[n]
            else:
                total += roman_to_int[n]


        
        return total + roman_to_int[s[-1]]
