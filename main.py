import subprocess
import shlex
import sys
import argparse
import json
from grading.testset import TestSet
from languages.languagemanager import LanguageManager

def main():
    lm = LanguageManager()

    # Define list of possible run arguments
    parser = argparse.ArgumentParser("s-engine")
    parser.add_argument("-s", "--solution", help="Filename of the soultion to be run.", required=True, type=str)
    parser.add_argument("-lang", "--language", help="Language to use to run the solution.", required=True, type=str)
    parser.add_argument("-t", "--test", help="Filename of the test set.", required=True, type=str)

    # Parse probided arguments
    args = parser.parse_args()
    solution_file = args.solution
    test_filename = args.test
    language = args.language

    # Open file that contains test set
    ts_file = open("problemlibrary/" + test_filename + ".json", "r")
    ts_json = ts_file.read()
    ts_file.close()

    test_set = TestSet.parse_json(ts_json)

    result = lm.run(language, "src_files/" + solution_file, test_set)

    # Write results of grading into the file
    filename_for_results = solution_file.split(".")[0] + ".json"
    f = open("results/" + filename_for_results, "w")
    f.write(result)
    f.close()

    print(result)


if __name__ == "__main__":
    main()
    