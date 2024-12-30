import re
class CheckPattern:
    def __init__(self , value:str) -> None:
        if value:
            self.value = value
        else:
            raise ValueError('insert correct value')

    def get_number_with_size(self , size:int)->int:
        number = ''
        count = 0
        for num in self.value:
            try:
                num = int(num)
                count += 1
            except:
                if count == size:
                    break
                else:
                    count = 0
                    number = ''
            else:
                number += str(num)
        try:
            return int(number)
        except:
            return 'not found pattern with this size'
    def check_is_number(self):
        for num in self.value.strip():
            try:
                number = int(num)
            except:
                return False
        else:
            return True
    def check_english_lang(self):
        pattern = r'^[A-Za-z0-9\s.,!?\'"()]*$'
        if re.fullmatch(pattern , self.value.strip()):
            return True
        else:
            return False
    def check_iranian_nation_code(self)->bool:
        if self.value.isdigit() and len(self.value) == 10:
            first_number = int(self.value[0])
            counter = 0
            total_sum = 0

            for i in range(1, 10):
                num = int(self.value[i - 1])
                if num == first_number:
                    counter += 1
                total_sum += num * (11 - i)

            r = total_sum % 11
            if r > 1:
                r = 11 - r

            if r == int(self.value[-1]) and counter < 9:
                return True

        return False
        
    def check_iranian_phone(self):
        pattern = r'^09(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9])-?[0-9]{3}-?[0-9]{4}$'
        if re.match(pattern , self.value):
            return True
        else:
            return False
    def check_email_pattern(self):
        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern , self.value):
            return True
        else:
            return False
    def check_password_upper_lower_number_specific(self):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
        if re.fullmatch(pattern , self.value):
            return True
        else:
            return False
    def check_password_letter_number(self):
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        if re.fullmatch(pattern , self.value):
            return True
        else:
            return False
    def check_password_upper_lower_number(self):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
        if re.fullmatch(pattern , self.value):
            return True
        else:
            return False
