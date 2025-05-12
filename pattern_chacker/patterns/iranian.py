import re


def check_iranian_nation_code(value:str)->bool:
        if value.isdigit() and len(value) == 10:
            first_number = int(value[0])
            counter = 0
            total_sum = 0

            for i in range(1, 10):
                num = int(value[i - 1])
                if num == first_number:
                    counter += 1
                total_sum += num * (11 - i)

            r = total_sum % 11
            if r > 1:
                r = 11 - r

            if r == int(value[-1]) and counter < 9:
                return True

        return False
def check_iranian_phone(value:str)-> bool:
        pattern = r'^09(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9])-?[0-9]{3}-?[0-9]{4}$'
        return bool(re.match(pattern , value.strip()))
