import subprocess
import shlex

def main():
    args = shlex.split("g++ -o src_files/a.out src_files/main.cpp")
    subprocess.Popen(args)
    subprocess.Popen("./src_files/a.out")

if __name__ == "__main__":
    main()