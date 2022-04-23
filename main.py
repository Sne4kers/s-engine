import subprocess
import shlex
from languages.languagemanager import LanguageManager

def main():
    lm = LanguageManager()
    lm.run("python3", "src_files/main.py")


if __name__ == "__main__":
    main()