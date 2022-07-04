# Sum of two number problem
# Example of forming test set in form of python file.
# TestSet class has method for transforming test set into json, 
# which is used for actual grading.

# You can also find JSON representation of declaring this test set

from grading.singletest import SingleTest 
from grading.blocktest import BlockTest 
from grading.testset import TestSet 

def get_test_set():
    test_set = TestSet(0, "Sum of two numbers")

    test_set.add_test(SingleTest("3\n26 36\n7 5\n4 -2\n", "62\n12\n2\n", 1, 1))
    test_set.add_test(SingleTest("2\n26 36\n7 5\n4 -2", "62\n12", 1, 1))

    block = BlockTest(3)
    block.add_test(SingleTest("3\n1 1\n2 3\n1 -2\n", "2\n5\n-1\n", 1, 1))
    block.add_test(SingleTest("3\n1 2\n2 3\n1 -2\n", "3\n5\n-1\n", 1, 1))
    block.add_test(SingleTest("3\n1 3\n2 3\n1 -2\n", "4\n5\n-1\n", 1, 1))

    test_set.add_test(block)
    return test_set