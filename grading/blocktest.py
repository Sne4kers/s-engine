from grading.test import Test

class BlockTest(Test):
    tests = {}
    def __init__(self, points):
        self.verdict = []
        self.points = points

    def add_test(self, test):
        self.tests[len(self.tests)] = test

    def evaluate(self, result, test_key):
        self.tests[test_key].evaluate(result)

        if not self.tests[test_key].result:
            self.result = self.tests[test_key].result

        for code in self.tests[test_key].verdict:
            if code not in self.verdict:
                self.verdict.append(code)
        

    def report(self):
        report = {}
        passed = True
        tests_in_report = {}

        for test in self.tests:
            tests_in_report[len(tests_in_report)] = self.tests[test].report()
            passed = passed and self.tests[test].result

        report["total_points"] = self.points
        
        if passed:
            report["result"] = "passed"
        else:
            report["result"] = "failed"
        report["verdict"] = self.verdict
        
        report["tests"] = tests_in_report
        return report
