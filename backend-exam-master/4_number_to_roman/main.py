"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "number can not be zero"
        if number > 3999:
            return "number out of range"
            
        list_of_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        for (n, roman) in list_of_roman:
            (d, number) = divmod(number, n)
            res += roman * d
        return res

if __name__ == "__main__":
    try:
        number = int(input().strip())
        sol = Solution()
        result = sol.number_to_roman(number)
        print(result)
    except ValueError:
        print("invalid input only integer")
