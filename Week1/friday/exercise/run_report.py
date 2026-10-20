"""Driver: build a Suite from sample rows and print every report format."""
from report_system import Suite, TextReporter, CsvReporter, TestResult

SAMPLE_ROWS = [
    {"test_id": "TC-001", "status": "PASS", "duration": 1.2},
    {"test_id": "TC-002", "status": "FAIL", "duration": 3.4, "message": "Timeout, retry failed"},
    {"test_id": "TC-003", "status": "pass", "duration": 0.8},
    {"test_id": "TC-004", "status": "SKIPPED"},
]
# Rows that SHOULD be rejected (bad id, bad status, negative duration).
BAD_ROWS = [
    {"test_id": "XX-9", "status": "PASS"},
    {"test_id": "TC-005", "status": "PSAS"},
    {"test_id": "TC-006", "status": "PASS", "duration": -1},
]


def main():
    # TODO 4.1: create Suite("Login") and add a TestResult.from_dict(row) for every
    #           row in SAMPLE_ROWS.
    suite = Suite("login")
    for row in SAMPLE_ROWS:
        suite.add(TestResult.from_dict(row))
    # TODO 4.2: for every row in BAD_ROWS, try to add it. Catch (ValueError, TypeError)
    #           and print "Rejected <test_id>: <error message>".
    for row in BAD_ROWS:
        try:
            suite.add(TestResult.from_dict())
        except ValueError as ve:
            print(f"Rejected {row["test_id"]}: {ve}")
        except TypeError as te:
            print(f"Rejected {row["test_id"]}: {te}")
    # TODO 4.3: put TextReporter(suite) and CsvReporter(suite) in ONE list, loop over
    #           it and print reporter.render() (same call, different output).
    reporters = [TextReporter(suite), CsvReporter(suite)]

    for report in reporters:
        print(report.render())

    # TODO 4.4: print "Results created:" and TestResult.how_many().
    print("Results created: ", TestResult.how_many())


if __name__ == "__main__":
    main()
