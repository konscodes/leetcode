import unittest
import code


class TestBasic(unittest.TestCase):

    def test_pivot(self):
        '''
        Test that it returns the correct list of multiples of 3 and 5 in the given range
        '''
        data = [1, 7, 3, 6, 5, 6]
        result = code.pivot(data)
        self.assertEqual(result, 3)

    def test_pivot2(self):
        '''
        Test that it returns the correct list of multiples of 3 and 5 in the given range
        '''
        data = [1, 2, 3]
        result = code.pivot(data)
        self.assertEqual(result, -1)

    def test_pivot3(self):
        '''
        Test that it returns the correct list of multiples of 3 and 5 in the given range
        '''
        data = [-1,-1,0,-1,-1,-1]
        result = code.pivot(data)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
