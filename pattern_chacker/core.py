class CheckPattern:
    def __init__(self , value:str) -> None:
        if value.strip():
            self.value = value.strip()
        else:
            raise ValueError('insert correct value')
    def get_number_with_size(self, size:int)-> int:
        from .patterns.basic import get_number_with_size
        return get_number_with_size(self.value, size)
    def check_is_number(self)-> bool:
        from .patterns.basic import check_is_number
        return check_is_number(self.value)
    def check_english_lang(self) -> bool:
        from .patterns.basic import check_english_lang
        return check_english_lang(self.value)
    def check_email_pattern(self) -> bool:
        from .patterns.basic import check_email_pattern
        return check_email_pattern(self.value)
    def check_iranian_nation_code(self) -> bool:
        from .patterns.iranian import check_iranian_nation_code
        return check_iranian_nation_code(self.value)
    def check_iranian_phone(self) -> bool:
        from .patterns.iranian import check_iranian_phone
        return check_iranian_phone(self.value)
    def check_password_upper_lower_number_specific(self) -> bool:
        from .patterns.password import check_password_upper_lower_number_specific
        return check_password_upper_lower_number_specific(self.value)
    def check_password_letter_number(self) -> bool:
        from .patterns.password import check_password_letter_number
        return check_password_letter_number(self.value)
    def check_password_upper_lower_number(self) -> bool:
        from .patterns.password import check_password_upper_lower_number
        return check_password_upper_lower_number(self.value)