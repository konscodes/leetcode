import unittest
import code


class TestBasic(unittest.TestCase):

    def test_merge(self):
        '''
        Test that it returns the correct list of multiples of 3 and 5 in the given range
        '''
        word1 = 'ab'
        word2 = 'pqrs'
        result = code.merge(word1, word2)
        self.assertEqual(result, 'apbqrs')


if __name__ == '__main__':
    unittest.main()
