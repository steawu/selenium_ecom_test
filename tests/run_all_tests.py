'''
run all tests all together and generate HTML test reports from unittest
'''

import unittest
import HtmlTestRunner
import os

test_suite = (unittest.TestLoader()).discover(start_dir='tests', pattern='test_*.py')  # run all tests under tests folder

# create a report directory upper lever, and put HTML reports in that folder
report_dir = os.path.join(os.path.dirname(__file__), "../reports")
os.makedirs(report_dir, exist_ok=True)    # prevent error if reports folder already exist

# set up HTML test runner, combine reports from multiple test classes into 1 file,
# and set up report name and show details
runner = HtmlTestRunner.HTMLTestRunner(
    output=report_dir,
    report_name="test_report",
    combine_reports=True,
    add_timestamp=True,
    verbosity=2
)

# execute all tests
runner.run(test_suite)

