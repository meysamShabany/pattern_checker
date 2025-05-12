import re

def get_number_with_size(value, size:int)->int:
        number = ''
        count = 0
        for num in value:
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
def check_is_number(value:str)-> bool:
        for num in value.strip():
            try:
                number = int(num)
            except:
                return False
        else:
            return True
def check_english_lang(value:str)-> bool:
        pattern = r'^[A-Za-z0-9\s.,!?\'"()]*$'
        return bool(re.fullmatch(pattern , value.strip())) 
    
def check_email_pattern(value:str)-> bool:
        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        return bool(re.fullmatch(pattern , value.strip())) 