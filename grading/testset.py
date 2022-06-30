import grading
import json

class TestSet():
    def __init__(self, testset_id):
        self.tests = []
        self.verdict = []
        self.total_points = 0
        self.testset_id = testset_id

    def add_test(self, test):
        self.tests.append(test)
        self.total_points += test.points

    def add_verdict(self, verdict_code):
        if verdict_code not in self.verdict:
            self.verdict.append(verdict_code)

    def report(self):
        report = {}
        earned_points = 0
        tests = {}
        counter = 0

        report["testset_id"] = self.testset_id
        report["total_points"] = self.total_points

        for test in self.tests:

            if isinstance(test, grading.singletest.SingleTest):
                if test.result:
                    earned_points += test.points

            if isinstance(test, grading.blocktest.BlockTest):
                passed = True
                for test_in_block in test.tests:
                    passed = passed and test.tests[test_in_block].result
                if passed:
                    earned_points += test.points

            for code in test.verdict:
                if code not in self.verdict:
                    self.verdict.append(code)

            tests[counter] = test.report()
            counter += 1

        report["earned_points"] = earned_points
        report["verdict"] = self.verdict
        report["tests"] = tests

        return json.dumps(report, indent=4)
        