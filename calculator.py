'''A class file for executing'''

from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer

class Calculator:
    '''A Calculator Class'''

    def __init__(self, filename, indices):
        self.filename = filename
        self.indices = indices

    def execute(self):
        '''Execute the data '''

        extractor = DataExtractor(self.filename)
        extracted_data = extractor.extract(self.indices)

        analyzer = DataAnalyzer(extracted_data)
        analyzed_data = analyzer.analyze()

        return analyzed_data
