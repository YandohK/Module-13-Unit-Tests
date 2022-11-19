import unittest
from datetime import datetime


class UnitTest(unittest.TestCase):

    def testA1(self):
        charSymbol = input('\nEnter stock symbol: ')
        self.assertLessEqual(len(charSymbol), 7, msg="Error:")
        self.assertTrue(charSymbol.isupper(), msg="Error:")
        
    def testA2(self):
        chartType = 1
        chartType = int(input('\nEnter your choice of chart type. Choose between 1 or 2: '))
        self.assertIn(chartType, [1,2], msg="Error:")

    def testA3(self):
        timeSeries = 1
        timeSeries = int(input('\nEnter time series option. Choose between 1-4: '))
        self.assertIn(timeSeries, [1,2,3,4], msg="Error:")

    def testA4(self):
        startDate = input('\nEnter the start date (format: YYYY-MM-DD): ')
        self.assertTrue(datetime.strptime(startDate, "%Y-%m-%d"))

    def testA5(self):
        endDate = input('\nEnter the end date (format: YYYY-MM-DD): ')
        self.assertTrue(datetime.strptime(endDate, "%Y-%m-%d"))

if __name__ == "__main__":
    unittest.main()
    unittest.TestLoader.sortTestMethodsUsing = None