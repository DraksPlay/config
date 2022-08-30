import unittest
from config.api import get

class TestApi(unittest.TestCase):

    def test_checker(self):
        self.assertEqual(get("../../config.ini"), True)

if __name__ == '__main__':
    unittest.main()