from languages.compiledlanguage import CompiledLanguage
from languages.language import Language

class CPP17(CompiledLanguage):

    def __init__(self):
        self.file_extensions = ["cpp"]
        self.cc = "cpp17"
        self.full_name = "C++ 17 / GCC 11.2.0"
        super().__init__()
    
    def compile_command(self, filepath):
        fileNameWithoutExtension = filepath.split("/")[-1].split(".")[0]
        filepathWithoutFile = "/".join(filepath.split("/")[:-1]) + "/"
        toBeGeneratedFilePath = filepathWithoutFile + fileNameWithoutExtension + ".out"
        return ["g++", "-o", toBeGeneratedFilePath, filepath]
    
    def run_command(self, filepath):
        fileNameWithoutExtension = filepath.split("/")[-1].split(".")[0]
        filepathWithoutFile = "/".join(filepath.split("/")[:-1]) + "/"
        toBeGeneratedFilePath = "./" + filepathWithoutFile + fileNameWithoutExtension + ".out"
        return [toBeGeneratedFilePath]

class Python(Language):
    def __init__(self):
        self.file_extensions = ["py"]
        self.cc = "python"
        self.full_name = "Python 3.10.4"
        super().__init__()
    
    def run_command(self, filepath):
        return ["python3", filepath]