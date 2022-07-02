# S-engine
## About
S-engine is a problem solution testing software.

S-engine is currently on very early stage of development but we expect it to support Python and C++ in early stages of development.

## How to run

S-engine takes only 2 parameters at the moment:

```
options:
  -h, --help            show this help message and exit
  -s SOLUTION, --solution SOLUTION
                        Filename of the soultion to be run.
  -lang LANGUAGE, --language LANGUAGE
                        Language to use to run the solution.
```

There are no default values for them, so both of them are reuired in order to run the check of the solution.

So, in order to run your solution (against the only test set available at the moment) put your soultion into `src_files` directory and run the `main.py` with options that fit your solution. The resutls will be available in the results folder and printed into the terminal.


## TODO
:white_check_mark: Basic run support  - application should be capable of running 

:white_check_mark: Basic run capability with custom input

:white_check_mark: Basic result verification of the output

:white_large_square: Result verification system with different output/input (file, stdout) as well as support for problems with multiple answers 

:white_large_square: Docker support

## Posible features

:white_large_square: Big-Oh calculator of provided script

## Running with Docker

Go to repository and build Docker iamge

```
docker build -t s-engine ./
```

After that I usually go one directory up, where I have directories for solution files and results, so it is easy to mount them when running Docker container with such command

```
docker run -it --name s-engine-instance-1 --mount type=bind,source="$(pwd)"/solutions,target=/usr/grading_sys/src_files --mount type=bind,source="$(pwd)"/results,target=/usr/grading_sys/results s-engine python3 main.py -s 2.py -lang python3
```

It example above, with `--mount type=bind,source="$(pwd)"/solutions,target=/usr/grading_sys/src_files --mount type=bind,source="$(pwd)"/results,target=/usr/grading_sys/results` we make sure that folders for results of checks and folder with solutions are mounted into the workdirectory of the container. After that we make regular call of python program and setup options for name of the solution file and language that is used to run this program.

<!-- :white_check_mark -->
