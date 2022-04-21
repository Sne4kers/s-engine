from languages.language import Language
from languages.compiledlanguage import CompiledLanguage
import subprocess
import languages.LanguageLibrary

LANG = []
EXTMAP = {}
EXTLIST = []

class LanguageManager():
    def __init__(self):
        for name, entity in languages.LanguageLibrary.__dict__.items():
            if not name.startswith('__') and name != "CompiledLanguage" and name != "Language":
                language = entity()
                LANG.append(language)
                for extension in language.file_extensions:
                    EXTMAP[extension] = language
                    EXTLIST.append(extension)

    def run(self, filepath):
        extension = filepath.split("/")[-1].split(".")[1]
        if extension not in EXTLIST:
            print(extension + " :")
            print("EXTENSION NOT SUPPORTED")
            return
        selected_language = EXTMAP[extension]
        
        if selected_language.__class__.__bases__[0].__name__ == "CompiledLanguage":
            compile_command = selected_language.compile_command(filepath)
            print(compile_command)
            compile_exec = subprocess.Popen(compile_command)
            compile_exec.wait()
            run_command = selected_language.run_command(filepath)
            print(run_command)
            run_exec = subprocess.Popen(run_command)

        else:
            run_command = selected_language.run_command(filepath)
            print(run_command)
            run_exec = subprocess.Popen(run_command)
