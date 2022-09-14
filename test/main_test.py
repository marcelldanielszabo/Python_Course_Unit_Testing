import unittest

from main import Sum_Three_Fnc

class TestSum(unittest.TestCase):
    
    def test_Sum_Three_Fnc(self):
        """
        Test that it can sum a list of integers
        """
        arg1 = 2
        arg2 = 3
        arg3 = 4
        result = Sum_Three_Fnc(arg1,arg2,arg3)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
    
    print("Everything Passed")