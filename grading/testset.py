import grading
import json

class TestSet():
    def __init__(self, testset_id, name):
        self.tests = []
        self.verdict = []
        self.name = name
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
        report["test_set_name"] = self.name
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
    
    def to_json(self):
        str_represent = {}
        str_represent["testset_id"] = self.testset_id
        str_represent["name"] = self.name

        tests_in_set = {}

        for test in self.tests:
            tests_in_set[len(tests_in_set)] = test.to_dict()

        str_represent["tests"] = tests_in_set

        return json.dumps(str_represent, indent=4)

    def parse_json(json_string):
        test_dict = json.loads(json_string)
        tests_in_report = []

        for key in test_dict["tests"]:
            test = test_dict["tests"][key]
            if "tests" in test:
                tests_in_report.append(grading.blocktest.BlockTest.parse_dict(test))
            else:
                tests_in_report.append(grading.singletest.SingleTest.parse_dict(test))

        to_return = TestSet(test_dict["testset_id"], test_dict["name"])
        for test in tests_in_report:
            to_return.add_test(test)
            
        return to_return


        