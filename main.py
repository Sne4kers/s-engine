import subprocess
import shlex
import sys
import argparse
from languages.languagemanager import LanguageManager

def main():
    lm = LanguageManager()

    parser = argparse.ArgumentParser("s-engine")
    parser.add_argument("-s", "--solution", help="Filename of the soultion to be run.", required=True, type=str)
    parser.add_argument("-lang", "--language", help="Language to use to run the solution.", required=True, type=str)
    #parser.add_argument("-o", "--output", help="Filename of the output of the check.", required=True, type=str)
    #parser.add_argument("-t", "--test", help="ID of the test set.", required=True, type=int)

    args = parser.parse_args()
    solution_file = args.solution
    #output_file = args.output
    #test_id = args.test
    language = args.language

    print(lm.run(language, "src_files/" + solution_file))


if __name__ == "__main__":
    main()
    