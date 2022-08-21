#Student Number: C1887413

"""Determine the minimum of all numbers in the file.

This program will take a CSV data file output the minimum of all the numbers in the file printed in the terminal

"""
from mrjob.job import MRJob
import csv


def csv_readlines(line):
    """Given a string CSV line, return a list of strings."""
    line = []
    for row in csv.reader(line, delimiter="\t"):
        line.append(row)

class MRfindMin(MRJob):
    def mapper(self, key, line):
        """Extracts value in lines"""
        for numbers in line.split(','):
            # convert the strings to integers.
            numbers = int(numbers)
            #return the KEY/VALUE.
            yield 1, numbers
        #Reduce function applied to all the values that share the same key.
    def reducer(self, key, numbers):
        title= "The minimum ="
        #calculate the minimum for the the numbers.
        numbers= min(numbers)
        yield title, numbers
             

if __name__ == '__main__':
    MRfindMin.run()


   

   