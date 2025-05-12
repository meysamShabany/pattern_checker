import re


def check_password_upper_lower_number_specific(value:str)-> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    return bool(re.fullmatch(pattern , value))
        
def check_password_letter_number(value:str)-> bool:
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
    return bool(re.fullmatch(pattern , value))
    
    
def check_password_upper_lower_number(value:str)-> bool:
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
        return bool(re.fullmatch(pattern , value))