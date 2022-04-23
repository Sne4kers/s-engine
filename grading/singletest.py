from grading.test import Test

class SingleTest(Test):
    test_input = ""
    test_output = ""
    def __init__(self, test_input, test_output, points):
        super().__init__(points)
        self.test_input = test_input
        self.test_output = test_output.strip()

    def evaluate(self, output):
        if output == self.test_output:
            self.result = True

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
            
        return report
        