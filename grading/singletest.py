from grading.test import Test
import json

class SingleTest(Test):
    test_input = ""
    test_output = ""
    time_limit = 0
    def __init__(self, test_input, test_output, points, time_limit):
        super().__init__(points)
        self.verdict = []
        self.time_limit = time_limit
        self.test_input = test_input
        self.test_output = test_output.strip()

    def evaluate(self, output):
        if output == self.test_output:
            self.result = True
        else:
            self.add_verdict("WA")
        
    def report(self):
        report = {
            "test_input" : self.test_input, 
            "test_output" : self.test_output, 
            "points" : self.points
            }

        if self.result == True:
            report["result"] = "passed"
        else:
            report["result"] = "failed"
            
        report["verdict"] = self.verdict

        return report

    def add_verdict(self, verdict_code):
        if verdict_code not in self.verdict:
            self.verdict.append(verdict_code)

    def to_dict(self):
        str_represent = {}
        str_represent["test_input"] = self.test_input
        str_represent["test_output"] = self.test_output
        str_represent["time_limit"] = self.time_limit
        str_represent["points"] = self.points

        return str_represent
    
    def parse_dict(json):
        test_dict = json
        return SingleTest(test_dict["test_input"], test_dict["test_output"], test_dict["points"], int(test_dict["time_limit"]))
