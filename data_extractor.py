'''A file to extract data'''

import re

class DataExtractor:
    '''A class for extracting data'''

    def __init__(self, filename):
        '''Take in csv filename as input'''
        self.filename = filename

    def extract(self, indices):
        '''Extracts Data'''

        final_data = []

        with open(self.filename, encoding="utf8") as file:
            lines = file.readlines()

            for line in lines:
                if line == '\n':
                    continue

                streamlined_line = line.strip().split()

                first_col = re.search('\d+', streamlined_line[0])
                if not first_col:
                    continue

                required_arguments = []

                for i, index in enumerate(indices):
                    column = ""
                    if i == 0:
                        column = streamlined_line[index]
                    else:
                        column = int(re.search('\d+', streamlined_line[index])[0])
                    required_arguments.append(column)

                final_data.append(tuple(required_arguments))

        return final_data
