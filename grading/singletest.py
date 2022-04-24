from grading.test import Test

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
        