# Amazon Automation Framework

This is a comprehensive automation framework for Amazon shopping, developed using Python, Selenium, and the Page Object Model (POM) for front-end testing.




# Usage
Configure AppConfig:

Set the Amazon URL in src/config/AppConfig.py.
Run Tests:

Execute tests using python run_tests.py.
View Test Report:

Check the HTML test report in the reports directory.

## Configure AppConfig:

Set the Amazon URL in `src/config/AppConfig.py`.

## Run Tests:

Execute tests using:

```bash
python run_tests.py
Check the HTML test report in the reports directory.

Test Cases
test_amazon_shopping.py
Test Case 1 (test_amazon_shopping_flow):
Searches for a laptop, adds it to the cart, and verifies the cart subtotal.
run_tests.py
Uses unittest and HTMLTestRunner to run the test suite and generate an HTML report.
Additional Information
The framework follows the Page Object Model for better maintainability and reusability of code.
Logging is implemented using LoggerUtil for better visibility into test execution.
