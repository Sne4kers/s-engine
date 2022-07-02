# S-engine
## About
S-engine is a problem solution testing software.

S-engine is currently on very early stage of development but we expect it to support Python and C++ in early stages of development.

## TODO
:white_check_mark: Basic run support  - application should be capable of running 

:white_check_mark: Basic run capability with custom input

:white_check_mark: Basic result verification of the output

:white_large_square: Result verification system with different output/input (file, stdout) as well as support for problems with multiple answers 

:white_large_square: Docker support

## Posible features

:white_large_square: Big-Oh calculator of provided script

##

Setup

'''
docker build -t s-engine ./
'''

After that run go in such directory so you can mount folder with soultion files into the /usr/grading_sys/src_files

'''
docker run -it --name devtest --mount type=bind,source="$(pwd)"/solutions,target=/usr/grading_sys/src_files s-engine python3 /usr/grading_sys/main.py -s 2.py -lang python3
'''

<!-- :white_check_mark -->
