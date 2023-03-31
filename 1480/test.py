import unittest
import code

class TestBasic(unittest.TestCase):
    def test_runningSum1(self):
        '''
        Test that it returns the correct list of running sum of given array
        '''
        data = [1,2,3,4]
        result = code.runningSum(data) 
        self.assertEqual(result, [1,3,6,10])
    
    def test_runningSum2(self):
        '''
        Test that it returns the correct list of running sum of given array
        '''
        data = [1,1,1,1,1]
        result = code.runningSum(data) 
        self.assertEqual(result, [1,2,3,4,5])
    
    def test_runningSum3(self):
        '''
        Test that it returns the correct list of running sum of given array
        '''
        data = [3,1,2,10,1]
        result = code.runningSum(data) 
        self.assertEqual(result, [3,4,6,16,17])

if __name__ == '__main__':
    unittest.main()