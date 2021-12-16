"""CSV Aggregation
   Thie module implements common Aggregation Operations on CSV Files.
   Author: Anthony Asta

"""
__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Anthony Asta'

import csv

class CSVFileAggregator(object):
    """
    CSVFileAggregator

    Class that implements aggregation types as methods

    Attributes:
        file_path: Valid file path for csv file
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def count_aggregation(self, column=None):
        """
        Perform the count aggregation -
         count the number of rows each value appears for a given column
        :type columns_agg: List
        :rtype: String
        """
        # dictionary to hold counts for a given column
        counts_for_column = {}

        with open(self.file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            print ("column by which we are aggregating: " + column)
            print ("fieldnames: " + str(reader.fieldnames))
            for row in reader:
                print (row)

                if column not in reader.fieldnames:
                    return "The column: " + column + " by which you are aggregating doesn't exist in this csv"
                # skip row if column doesn't have a value
                elif not row[column]:
                    print ("skip row")
                # see if the value doesn't exist in the counts dict add it with a value = 1
                elif row[column] not in counts_for_column.keys():
                    print("new value for column: " + row[column])
                    counts_for_column[row[column]] = 1
                # if it exists increment count in dictionary
                elif row[column] in counts_for_column.keys():
                    counts_for_column[row[column]] = counts_for_column[row[column]] + 1
        return str(counts_for_column)





def main():
    print("Hello World!")
    aggregator = CSVFileAggregator("./CSVAggregator/CSVAggregatorTestData.csv")
    aggregation_output = aggregator.count_aggregation("name")
    print (aggregation_output)

if __name__ == "__main__":
    main()