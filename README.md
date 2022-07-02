# S-engine
## About
S-engine is a problem solution testing software.

In order to run solution against availble test set, provide as arguments solution filename and language to use. As a result of grading process, S-engine will give you json file with info about each test used for grading and verdicts on them if they were failed, such as WA, RE, TL("wrong answer", "runtime error", "time limit").

Right now it is not possible to use different test sets, so all solutions will be graded against hte onlt available set for "Sum of two numbers N-times".

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

There are no default values for them, so both of them are required in order to run the check of the solution.

So, in order to run your solution (against the only test set available at the moment) put your soultion into `src_files` directory and run the `main.py` with options that fit your solution. The resutls will be available in the `results` folder and printed into the terminal.

## How to add custom test set

S-engine has a test for "Sum of two numbers N-times" problem - you can check it at `problemlibrary` folder. Probably, the way test sets are provided will be changed.

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


## TODO
:heavy_check_mark: Basic run support  - application should be capable of running solutions. 

:heavy_check_mark: S-engine is capable of running solutions with custom input

:heavy_check_mark: S-engine can verify output of the program.

:heavy_check_mark: S-engine provides file with results of grading, where info about every test used for grading is listed.

:heavy_check_mark: S-engine can run block tests. Block test is a test that contains multiple fails. Block test is considered passed, when all tests that are contained in it were passed.

:heavy_check_mark: Docker support.

:white_large_square: S-engine can grade test that can have multiple answers.

## Posible features

:white_large_square: Big-Oh calculator of provided script.

<!-- :white_check_mark -->
