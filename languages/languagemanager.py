from languages.language import Language
from languages.compiledlanguage import CompiledLanguage
import subprocess
import languages.LanguageLibrary
from grading.test import Test
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
        
        test = Test("Yehor", "Hello, Yehor!", 1)


        if selected_language.__class__.__bases__[0].__name__ == "CompiledLanguage":
            compile_command = selected_language.compile_command(filepath)
            print(compile_command)
            compile_exec = subprocess.Popen(compile_command)
            compile_exec.wait()
            run_command = selected_language.run_command(filepath)
            print(run_command)

            run_exec = subprocess.Popen(run_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            result = run_exec.communicate(input=test.test_input.encode())[0]
            print(result)
            if result.decode().strip() == test.test_output:
                print("Successfull")
            else:
                print("Failed")

        else:
            run_command = selected_language.run_command(filepath)
            print(run_command)
            run_exec = subprocess.Popen(run_command)
