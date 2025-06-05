# Selenium E-Commerce Test Suite for SauceDemo

This project is an automated test suite built using **Python**, **Selenium WebDriver**, and **unittest** 
for testing the e-commerce demo site [SauceDemo](https://www.saucedemo.com). It includes tests for login, product interactions, cart functionality, 
and the full checkout process. After running all tests, it will generate a HTML report in reports folder.

## Tech Stack
- Python 3.13
- Selenium WebDriver
- unittest 
- HtmlTestRunner 
- ChromeDriver (latest version)

## How to Run
1. Create and activate virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
2. Install dependencies
   ```bash
    pip install -r requirements.txt
3. Run all tests
   ```bash
   python run_all_tests.py
