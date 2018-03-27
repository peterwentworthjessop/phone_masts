import csv
import sys

## This class will implement the functionality required in the phone mast test.
## I will use the Python csv module to read the file into a list, mast_list.
## The data is not normalized and contains spelling errors,
## but no attempt is made to clean it up because I take the note
## in the objective to mean that misspelt tenant names shall be treated
## as distinct, individual names.
## The first line is a header, and is discarded.
class Masts:
    def __init__(self):
        self.mast_list = []
        self.ordered_list = []

    def read_in(self, file_name='c:\\phone_mast_data\\Mobile Phone Masts.csv'):
        '''Read a file into the mast list, removing the header'''
        f = open(file_name, 'r')
        reader = csv.reader(f)
        self.mast_list = list(reader)[1:]
        f.close()
        
    def requirement_1(self):
        '''Produce a list sorted by current rent'''
        ## Apply a list comprehension to the whole list,
        ## copying the current rent field to the start of the row as a number.
        temp_list = [[float(row[10])]+row for row in self.mast_list]
        ## sort this temporary list
        temp_list.sort()
        ## Now remove the copied field form the start of each row.
        self.ordered_list = [row[1:] for row in temp_list]
        ## Print the first 5 rows to the console
        for row in self.ordered_list[0:5]:
            print(row)

