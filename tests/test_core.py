import unittest
from pattern_chacker import CheckPattern

class TestCheckPattern(unittest.TestCase):
    def test_check_is_number(self):
        checker = CheckPattern("123")
        self.assertTrue(checker.check_is_number())
        checker = CheckPattern("12a3")
        self.assertFalse(checker.check_is_number())
    def test_check_iranian_phone(self):
        checker = CheckPattern("09121235643")
        self.assertTrue(checker.check_iranian_phone())
        checker = CheckPattern("01114563421")
        self.assertFalse(checker.check_iranian_phone())
        
if __name__ == "__main__":
    unittest.main()