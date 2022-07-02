from languages.language import Language
from languages.compiledlanguage import CompiledLanguage
from grading.singletest import SingleTest 
from grading.blocktest import BlockTest 
from grading.testset import TestSet 
import os.path
import os

import problemlibrary.sum_of_two_numbers
import languages.LanguageLibrary
import subprocess
import time

LANG = []
NAMEMAP = {}
EXTLIST = []

class LanguageManager():
    def __init__(self):
        for name, entity in languages.LanguageLibrary.__dict__.items():
            if not name.startswith('__') and name != "CompiledLanguage" and name != "Language":
                language = entity()
                LANG.append(language)
                NAMEMAP[language.cc] = language
                for extension in language.file_extensions:
                    EXTLIST.append(extension)

    def run(self, language, filepath):
        # Check if language is supported
        if language in NAMEMAP:
            selected_language = NAMEMAP[language]
        else:
            print("LANGUAGE IS NOT SUPPORTED")
            return "LANGUAGE IS NOT SUPPORTED"
        
        if not os.path.isfile(os.getcwd() + "/" + filepath):
            print(filepath)
            return "NO SUCH FILE"
        
        # Load test set - will be replaced with automatic load in future
        
        test_set = problemlibrary.sum_of_two_numbers.get_test_set()

        # Compile program first if language uses compiler
        if isinstance(selected_language, CompiledLanguage):
            compile_command = selected_language.compile_command(filepath)
            compile_exec = subprocess.Popen(compile_command)
            compile_exec.wait()
            if compile_exec.returncode == 1:
                test_set.add_verdict("CE")
                return test_set.report()

        run_command = selected_language.run_command(filepath)

        # For each test run the program and test with available input
        for test in test_set.tests:

            if isinstance(test, SingleTest):
                run_exec = subprocess.Popen(run_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    result = run_exec.communicate(input=test.test_input.encode(), timeout=test.time_limit)[0]
                    if run_exec.returncode != 0:
                        test.add_verdict("RE")
                    else:
                        test.evaluate(result.decode().strip())
                except subprocess.TimeoutExpired:
                    run_exec.kill()
                    test.add_verdict("TL")

            if isinstance(test, BlockTest):
                for key_test_in_block in BlockTest.tests:
                    test_in_block = test.tests[key_test_in_block]
                    run_exec = subprocess.Popen(run_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        result = run_exec.communicate(input=test_in_block.test_input.encode(), timeout=test_in_block.time_limit)[0]
                        if run_exec.returncode != 0:
                            test_in_block.add_verdict("RE")
                        else:
                            test.evaluate(result.decode().strip(), key_test_in_block)
                    except subprocess.TimeoutExpired:
                        run_exec.kill()
                        test_in_block.add_verdict("TL")

        # Print the report
        return test_set.report()
