import grading
import json

class TestSet():
    testset_id = 0
    tests = []
    total_points = 0
    def __init__(self, testset_id):
        self.testset_id = testset_id

    def add_test(self, test):
        self.tests.append(test)
        self.total_points += test.points

    def report(self, short_report):
        report = {}
        earned_points = 0
        tests = {}
        counter = 0

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

            tests[counter] = test.report()
            counter += 1

        report["testset_id"] = self.testset_id
        report["total_points"] = self.total_points
        report["earned_points"] = earned_points
        
        if not short_report:
            report["tests"] = tests

        return json.dumps(report, indent=4)
        