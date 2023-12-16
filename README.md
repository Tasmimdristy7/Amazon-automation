# Amazon Automation Framework

This is a comprehensive automation framework for Amazon shopping, developed using Python, Selenium, and the Page Object Model (POM) for front-end testing.

## Project Structure

```plaintext
amazon_automation_framework/
|-- src/
|   |-- config/
|       |-- AppConfig.py
|
|-- tests/
|   |-- test_amazon_shopping.py
|
|-- pages/
|   |-- base_page.py
|   |-- home_page.py
|   |-- search_results_page.py
|   |-- product_page.py
|   |-- cart_page.py
|
|-- utils/
|   |-- LoggerUtil.py
|
|-- run_tests.py
|-- requirements.txt
# Usage

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
