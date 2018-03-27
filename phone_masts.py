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

    def read_in(self, file_name='c:\\phone_mast_data\\Mobile Phone Masts.csv'):
        '''Read a file into the mast list, removing the header'''
        f = open(file_name, 'r')
        reader = csv.reader(f)
        self.mast_list = list(reader)[1:]
        f.close()
