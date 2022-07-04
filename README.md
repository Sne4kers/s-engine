# S-engine
## About
S-engine is a problem solution testing software.

In order to run solution against availble test set, provide as arguments solution filename and language to use. As a result of grading process, S-engine will give you json file with info about each test used for grading and verdicts on them if they were failed, such as CE, WA, RE, TL("compilation error", "wrong answer", "runtime error", "time limit").

You can find few examples for test sets and solutions to run the program. You can
find them in corresponding folders. They are designed to fit two problems - 
"Sum of two numbers" and "GCD of two numbers". Feel free to run them and check
results of grading.

## How to run

S-engine takes only 2 parameters at the moment:

```
usage: s-engine [-h] -s SOLUTION -lang LANGUAGE -t TEST

options:
  -h, --help            show this help message and exit
  -s SOLUTION, --solution SOLUTION
                        Filename of the soultion to be run.
  -lang LANGUAGE, --language LANGUAGE
                        Language to use to run the solution.
  -t TEST, --test TEST  Filename of the test set.
```

There are no default values for them, so both of them are required in order to run the check of the solution.

So, in order to run your solution put your soultion into `src_files` directory and test set in form of JSON in `problemlibrary` directory and run the `main.py` with options that fit your solution. The resutls will be available in the `results` folder and printed into the terminal.

## Example of starting grading

Example of starting grading if you want to test the solution with filename `1.cpp`
against test set `sum_of_two_numbers.json` and soluton is obviously using Python.

```
python3 main.py -s 1.cpp -lang cpp17 -t sum_of_two_numbers
```

Results will always appear in file that has same name as the solution, but with 
`.json` file extension.

## Example of the execution result

```
{
    "testset_id": 0,
    "test_set_name": "Sum of two numbers",
    "total_points": 5,
    "earned_points": 2,
    "verdict": [
        "WA"
    ],
    "tests": {
        "0": {
            "test_input": "3\n26 36\n7 5\n4 -2\n",
            "test_output": "62\n12\n2",
            "points": 1,
            "result": "passed",
            "verdict": []
        },
        "1": {
            "test_input": "2\n26 36\n7 5\n4 -2",
            "test_output": "62\n12",
            "points": 1,
            "result": "passed",
            "verdict": []
        },
        "2": {
            "total_points": 3,
            "result": "failed",
            "verdict": [
                "WA"
            ],
            "tests": {
                "0": {
                    "test_input": "3\n1 1\n2 3\n1 -2\n",
                    "test_output": "2\n5\n-1",
                    "points": 1,
                    "result": "passed",
                    "verdict": []
                },
                "1": {
                    "test_input": "3\n1 2\n2 3\n1 -2\n",
                    "test_output": "3\n5\n-1",
                    "points": 1,
                    "result": "passed",
                    "verdict": []
                },
                "2": {
                    "test_input": "3\n1 3\n2 3\n1 -2\n",
                    "test_output": "4\n5\n-1",
                    "points": 1,
                    "result": "failed",
                    "verdict": [
                        "WA"
                    ]
                }
            }
        }
    }
}
```

## How to add custom test set

S-engine has a test for "Sum of two numbers N-times" problem - you can check it at `problemlibrary` folder. Probably, the way test sets are provided will be changed.

## Running with Docker

Go to repository and build Docker iamge

```
docker build -t s-engine ./
```

After that I usually go one directory up, where I have directories for solution files and results, so it is easy to mount them when running Docker container with such command

```
docker run -it --name s-engine-instance-1 --mount type=bind,source="$(pwd)"/solutions,target=/usr/grading_sys/src_files --mount type=bind,source="$(pwd)"/results,target=/usr/grading_sys/results --mount type=bind,source="$(pwd)"/problemlibrary,target=/usr/grading_sys/problemlibrary s-engine python3 main.py -s 3.py -lang python3 -t gcd_of_two_numbers

```

It example above, with `--mount type=bind,source="$(pwd)"/solutions,target=/usr/grading_sys/src_files --mount type=bind,source="$(pwd)"/results,target=/usr/grading_sys/results --mount type=bind,source="$(pwd)"/problemlibrary,target=/usr/grading_sys/problemlibrary ` we make sure that folders for results of checks, folder with solutions and test sets are mounted into the workdirectory of the container. After that we make regular call of python program and setup options for name of the solution file and language that is used to run this program.


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
