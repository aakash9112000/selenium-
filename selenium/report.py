print("hello")

import unittest
# import GoogleTest
# import WikiTest
import os

# Import the HTMLTestRunner Module
import HtmlTestRunner

current_directory = os.getcwd()

class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_GoogleWiki_Search(self):

        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(report_by_searchb.MyGoogleTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(report_by_search.MyGoogleTest),
            # unittest.defaultTestLoader.loadTestsFromTestCase(WikiTest.WikipediaSeachTest)
        ])

        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )

        html_runner.run(consolidated_test)

if __name__ == '__main__':
    unittest.main()