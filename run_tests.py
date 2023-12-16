import unittest
import HTMLTestRunner
from test_amazon_shopping import TestAmazonShopping

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add test modules
    suite.addTests(loader.loadTestsFromModule(TestAmazonShopping))

    # Specify report file
    report_file = open("reports/test_report.html", "w")

    # Run the tests and generate the HTML report
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=report_file,
        title='Amazon Shopping Test Report',
        description='Test results'
    )
    runner.run(suite)

    report_file.close()
