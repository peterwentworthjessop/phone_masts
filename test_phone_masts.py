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
        
        
    def test_requirement_1(self):
        '''Test first requirement'''
        expected = [['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7', 'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', '20', '6600.00'],
         ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'],
         ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'],
         ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'],
         ['Cottingley Towers', 'Leeds', '', '', 'LS11', 'Cottingley Towers-WYK0052', 'Everything Everywhere Ltd', '28 Jan 2008', '27 Jan 2018', '10', '12750.00']
        ]
        ordered_list = self.masts.requirement_1()
        self.assertEqual(ordered_list[0:5], expected)
        
    def test_requirement_2(self):
        '''Test second requirement'''
        expected = ([         ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'],
         ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'],
         ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'],
         ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) - Block 2, WYK 0414', 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd', '21 Aug 2007', '20 Aug 2032', '25', '12750.00']
         ],
         46500.0)
        years_25_list, rent =  self.masts.requirement_2()
        self.assertEqual((years_25_list, rent), expected)

if __name__ == '__main__':
    unittest.main()
