from grading.test import Test

class SingleTest(Test):
    test_input = ""
    test_output = ""
    def __init__(self, test_input, test_output, points):
        super().__init__(points)
        self.test_input = test_input
        self.test_output = test_output

    def evaluate(self, output):
        if output == self.test_output:
            self.passed = True