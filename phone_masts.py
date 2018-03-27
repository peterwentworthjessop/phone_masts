import csv
import sys

## This class will implement the functionality required in the phone mast test.
## I will use the Python csv module to read the file into a list, mast_list.
## The data is not normalized and contains spelling errors,
## but no attempt is made to clean it up because I take the note
## in the objective to mean that misspelt tenant names shall be treated
## as distinct, individual names.
## The first line is a header, and is discarded.
##
## Constants to index the row
##
PROPERTY_NAME = 0
ADDRESS_1 = 1
ADDRESS_2 = 2
ADDRESS_3 = 3
ADDRESS_4 = 4
UNIT_NAME = 5
TENANT_NAME = 6
LEASE_START_DATE = 7
LEASE_END_DATE = 8
LEASE_YEARS = 9
CURRENT_RENT = 10

class Masts:
    def __init__(self):
        self.mast_list = []

    def read_in(self, file_name='c:\\phone_mast_data\\Mobile Phone Masts.csv'):
        '''Read a file into the mast list, removing the header'''
        f = open(file_name, 'r')
        reader = csv.reader(f)
        self.mast_list = list(reader)[1:]
        f.close()
        
    ## Requirement methods will return the data produced for the requirement.
    def requirement_1(self):
        '''Produce a list sorted by current rent'''
        ## Apply a list comprehension to the whole list,
        ## copying the current rent field to the start of the row as a number.
        temp_list = [[float(row[CURRENT_RENT])]+row for row in self.mast_list]
        ## sort this temporary list
        temp_list.sort()
        ## Now remove the copied field form the start of each row.
        ordered_list = [row[1:] for row in temp_list]
        ## Print the first 5 rows to the console
        for row in ordered_list[0:5]:
            print(row)
        return ordered_list
        
    def requirement_2(self):
        '''Produce a list where the lease years are 25'''
        years_25_list = [row for row in self.mast_list if row[LEASE_YEARS] == '25']
        total_rent = 0.0
        for row in years_25_list:
            print(row)
            total_rent += float(row[CURRENT_RENT])
        print(total_rent)
        return(years_25_list, total_rent)
        
    def requirement_3(self):
        '''Produce a dictionary of tenants'''
        tenants = {}
        for row in self.mast_list:
            tenant = row[TENANT_NAME]
            if tenant in tenants:
                tenants[tenant] += 1
            else:
                tenants[tenant] = 1
        keys = list(tenants.keys())
        keys.sort()
        for key in keys:
            print('Tenant %s has %d masts' % (key, tenants[key]))
        return tenants
