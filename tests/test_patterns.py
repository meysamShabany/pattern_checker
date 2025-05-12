import unittest
from pattern_chacker.patterns.basic import check_english_lang
from pattern_chacker.patterns.iranian import check_iranian_nation_code

class TestCheckPattern(unittest.TestCase):
    def test_check_english_lang(self):
        self.assertTrue(check_english_lang("Hello World"))
        self.assertFalse(check_english_lang("سلام"))
    def test_check_iranian_nation_code(self):
        self.assertTrue(check_iranian_nation_code("0650451252"))
        self.assertFalse(check_iranian_nation_code("1180564525"))
        
if __name__ == "__main__":
    unittest.main()