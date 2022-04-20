import subprocess
import shlex
from languages.languagemanager import LanguageManager

def main():
    lm = LanguageManager()
    lm.run("src_files/main.cpp")


if __name__ == "__main__":
    main()