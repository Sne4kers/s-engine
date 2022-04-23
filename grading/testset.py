import grading

class TestSet():
    testset_id = 0
    tests = []
    total_points = 0
    def __init__(self, testset_id):
        self.testset_id = testset_id

    def add_test(self, test):
        self.tests.append(test)
        self.total_points += test.points