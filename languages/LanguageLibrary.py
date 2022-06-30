from languages.compiledlanguage import CompiledLanguage
from languages.language import Language
'''

This file contains "singletons" for all available languages.

Every class of the language should inherit CompiledLanguage(in case solution
requires pre-run compilation) or Language(if language uses intepreter).

It's recommended to only define basic info about the language in __init__ and
overload run_command and compile_command(in CompiledLanguage) methods.

Every solution that arrives should use language present here. In case if
there is no such language error will be thrown.

'''


class CPP17(CompiledLanguage):

    def __init__(self):
        super().__init__()
        self.file_extensions = ["cpp"]
        self.cc = "cpp17"
        self.full_name = "C++ 17 / GCC 11.2.0"
    
    def compile_command(self, filepath):
        filename_without_extension = filepath.split("/")[-1].split(".")[0]
        filepath_without_file = "/".join(filepath.split("/")[:-1]) + "/"
        to_be_generated_filepath = filepath_without_file + filename_without_extension + ".out"
        return ["g++", "-o", to_be_generated_filepath, filepath, "-std=c++17"]
    
    def run_command(self, filepath):
        filename_without_extension = filepath.split("/")[-1].split(".")[0]
        filepath_without_file = "/".join(filepath.split("/")[:-1]) + "/"
        to_be_generated_filepath = "./" + filepath_without_file + filename_without_extension + ".out"
        return [to_be_generated_filepath]

class Python(Language):
    def __init__(self):
        super().__init__()
        self.file_extensions = ["py"]
        self.cc = "python3"
        self.full_name = "Python 3.10.4"
    
    def run_command(self, filepath):
        return ["python3", filepath]
        