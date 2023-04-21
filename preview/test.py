import unittest
import code


class TestBasic(unittest.TestCase):

    def test_find_multiples(self):
        '''
        Test that it returns the correct list of multiples of 3 and 5 in the given range
        '''
        data = 10
        result = code.find_multiples(data)
        self.assertEqual(result, [3, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
