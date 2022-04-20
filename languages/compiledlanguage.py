from languages.language import Language

class CompiledLanguage(Language):
    def __init__(self):
        super().__init__()

    def run_command(self, filepath):
        pass

    def compile_command(self, filepath):
        pass