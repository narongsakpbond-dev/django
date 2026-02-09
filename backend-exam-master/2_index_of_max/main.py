"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> list[int] | str:
        if not numbers:
            return "list can not blank"

        max_value = max(numbers)
        max_index = []
        for i in range(len(numbers)):
            if numbers[i] == max_value:
                max_index.append(i)
        return max_index


if __name__ == "__main__":
    solution = Solution()
    print(solution.find_max_index([1, 2, 1, 3, 5, 6, 4]))
    print(solution.find_max_index([]))
