import unittest
import phone_masts

class TestPhoneMasts(unittest.TestCase):
    
    def setUp(self):
        '''Read csv file into a new Masts object'''
        self.masts = phone_masts.Masts()
        self.masts.read_in()

    def test_read_in1(self):
        '''Check length of default file'''
        self.assertEqual(len(self.masts.mast_list), 42)

    def test_read_in2(self):
        '''Read in test file with 1 row'''
        test_list = [['Beecroft Hill', 'Broad Lane', '', '', 'LS13', 'Mast 1', 'Tenant 1', '01 Mar 1994', '28 Feb 2058', '64', '50.00']]
        self.masts.read_in('c:\\phone_mast_data\\Test_Masts1.csv')
        self.assertEqual(self.masts.mast_list, test_list)


if __name__ == '__main__':
    unittest.main()
