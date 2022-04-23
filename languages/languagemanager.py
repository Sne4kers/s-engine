from languages.language import Language
from languages.compiledlanguage import CompiledLanguage
import languages.LanguageLibrary
from grading.singletest import SingleTest 
from grading.testset import TestSet 
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
        if language in NAMEMAP:
            selected_language = NAMEMAP[language]
        else:
            print("LANGUAGE IS NOT SUPPORTED")
            return
        
        testSet = TestSet(1)
        testSet.add_test(SingleTest("3\n26 36\n7 5\n4 -2\n", "62\n12\n2\n", 1))
        testSet.add_test(SingleTest("2\n26 36\n7 5\n4 -2", "62\n12", 1))


        if selected_language.__class__.__bases__[0].__name__ == "CompiledLanguage":
            compile_command = selected_language.compile_command(filepath)
            compile_exec = subprocess.Popen(compile_command)
            compile_exec.wait()

        run_command = selected_language.run_command(filepath)

        for test in testSet.tests:
            run_exec = subprocess.Popen(run_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            result = run_exec.communicate(input=test.test_input.encode())[0]
            test.evaluate(result.decode().strip())
        
        print(testSet.report(False))