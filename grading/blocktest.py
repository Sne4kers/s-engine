from grading.test import Test
from grading.singletest import SingleTest
import json

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
    
    def to_dict(self):
        str_represent = {}
        tests_in_report = {}

        for test in self.tests:
            tests_in_report[len(tests_in_report)] = self.tests[test].to_dict()

        str_represent["total_points"] = self.points
        
        str_represent["tests"] = tests_in_report
        return str_represent

    def parse_dict(dict):
        tests_in_report = []

        for key in dict["tests"]:
            test = dict["tests"][key]
            if "tests" in test:
                tests_in_report.append(BlockTest.parse_dict(test))
            else:
                tests_in_report.append(SingleTest.parse_dict(test))

        to_return = BlockTest(dict["total_points"])
        for test in tests_in_report:
            to_return.add_test(test)
            
        return to_return


