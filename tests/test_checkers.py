import unittest
from config.checkers import checker

class TestCheckers(unittest.TestCase):

    def test_checker(self):
        self.assertEqual(checker("config.ini", suffix=".ini"), True)

if __name__ == '__main__':
    unittest.main()