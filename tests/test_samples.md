
# EWB Phishing URL Awareness Checker
## Test Results

Python version: 3.14.10
Operating System: Windows 11
Test Date: 10 November 2026

| # | Sample URL | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | IP address + HTTP warnings | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | @ symbol + HTTP warnings | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Hostname segments warning | PASS |
| 5 | https://xn--example.invalid/ | Punycode warning | Punycode warning detected | PASS |

## Test Summary

Total Tests: 5
Passed: 5
Failed: 0

## Observations

1. The program successfully detected all six selected URL warning signs across the implemented checks.
2. The program can analyze multiple URLs without restarting.
3. The program displays explanations for detected warning signs.
4. The program does not open websites or send URL data anywhere.
5. No warning signs detected does not guarantee that a URL is safe.

## Conclusion

All five official sample URL tests passed successfully.
The enhanced Phishing URL Awareness Checker is working as expected.
