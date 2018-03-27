import csv
import sys
import time

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

## It would have been good to use a GUI or Web framework
## to provide a front end for this program,
## but I am keeping it simple by providing a command-line menu.

def main():
    ## If the file path is not provided as the first argument
    ## read in the default file.
    masts = Masts()
    if len(sys.argv) > 1:
        masts.read_in(sys.argv[1])
    else:
        masts.read_in()
    ## A menu to run each requirement
    ##
    menu ='\nMenu\n----\n\n'+\
    '1 - first requirement\n2 - second requirement\n3 - third requirement\n'+\
        '4 - fourth requirement\n5 - exit.\n'
    answer = '1'
    while answer != 5:
        print(menu)
        answer = input('Enter a number 1-5: ').strip()
        if answer == '1':
            result = masts.requirement_1()
        elif answer == '2':
            result = masts.requirement_2()
        elif answer == '3':
            result = masts.requirement_3()
        elif answer == '4':
            result = masts.requirement_4()
        else:
            answer = '5'
            break

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
            ## Set to 1 in the first instance, or increment
            if tenant in tenants:
                tenants[tenant] += 1
            else:
                tenants[tenant] = 1
        keys = list(tenants.keys())
        keys.sort()
        for key in keys:
            print('Tenant %s has %d masts' % (key, tenants[key]))
        return tenants
        
    def requirement_4(self):
        '''Produce a list of data for a time period'''
        ## Get time limits as seconds
        lower_limit = time.mktime(time.strptime('01 Jun 1999', "%d %b %Y"))
        upper_limit = time.mktime(time.strptime('31 Aug 2007', "%d %b %Y"))
        ##
        restricted_list = []
        for row in self.mast_list:
            start = time.strptime(row[LEASE_START_DATE], "%d %b %Y")
            end = time.strptime(row[LEASE_END_DATE], "%d %b %Y")
            start_secs = time.mktime(start)
            ## check for start date within limits
            if start_secs >= lower_limit and start_secs <= upper_limit:
                ## format dates as DD/MM/YYYY
                formatted_row = row
                formatted_row[LEASE_START_DATE] = time.strftime('%d/%m/%Y', start)
                formatted_row[LEASE_END_DATE] = time.strftime('%d/%m/%Y', end)
                restricted_list.append(formatted_row)
        for row in restricted_list:
            print(row)
        return restricted_list
        
if __name__ == '__main__':
    main()