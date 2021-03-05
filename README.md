# Python FizzBuzz

This segment is intended to be used to teach how to use the Python debugger along with Pytest.

## Setup

1.  Create a virtual environment

```bash
$ python3 -m venv venv
```

2.  Activate the environment

```bash
$ source venv/bin/activate
```

3.  Install the dependencies


```bash
pip install -r requirements.txt
```

You can now run the tests with the command

```bash
$ pytest
```

## FizzBuzz Function

`fizzbuzz` is a function which returns the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

**Example:**


```
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

## Implementation Not working

However this function is not passing all it's tests.  Use the debugger to make the program pass the given tests.