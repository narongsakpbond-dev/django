"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    thai_number = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
    unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")

    def unit_process(self, val: str) -> str:
        length = len(val) > 1
        result = ""

        for index, current in enumerate(map(int, val)):
            if current == 0:
                continue
                
            # เพิ่มหน่วย (สิบ, ร้อย, พัน, หมื่น, แสน)
            if index > 0:
                result = self.unit[index] + result
            
            # กรณีพิเศษ: หลักหน่วยเป็น 1 และมีหลักอื่นด้วย -> "เอ็ด"
            if index == 0 and current == 1 and length:
                result += "เอ็ด"
            # กรณีพิเศษ: หลักสิบเป็น 2 -> "ยี่"
            elif index == 1 and current == 2:
                result = "ยี่" + result
            # กรณีพิเศษ: หลักสิบเป็น 1 -> ไม่ต้องอ่านเลข (เช่น 10 = "สิบ" ไม่ใช่ "หนึ่งสิบ")
            elif index == 1 and current == 1:
                pass
            # กรณีปกติ: อ่านตัวเลขตามปกติ
            else:
                result = self.thai_number[current] + result

        return result

    def thai_num2text(self, number: int) -> str:
        s_number = str(number)[::-1]
        n_list = [s_number[i:i + 6].rstrip("0") for i in range(0, len(s_number), 6)]
        result = self.unit_process(n_list.pop(0))

        for i in n_list:
            result = self.unit_process(i) + "ล้าน" + result

        return result

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10_000_000:
            return "number out of range"

        if number == 0:
            return "ศูนย์"

        return self.thai_num2text(number)


if __name__ == "__main__":
    try:
        raw = input().strip()
        raw = raw.replace(",", "")
        number = int(raw)
        sol = Solution()
        result = sol.number_to_thai(number)
        print(result)
    except ValueError:
        print("invalid input only integer")
