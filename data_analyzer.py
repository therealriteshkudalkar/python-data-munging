'''Data Analyzer'''

import sys

class DataAnalyzer:
    '''A class for analyzing data'''

    def __init__(self, extracted_data):
        self.data = extracted_data

    def analyze(self):
        '''Analyzes data'''

        min_grad = sys.maxsize
        min_grad_first_col = ""

        for first_col, minimum, maximum  in self.data:
            # convert remaining columns into ints
            curr_diff = abs(minimum - maximum)
            if curr_diff < min_grad:
                min_grad = curr_diff
                min_grad_first_col = first_col

        return min_grad_first_col
