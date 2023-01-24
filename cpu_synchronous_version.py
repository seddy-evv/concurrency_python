"""
Code example with CPU-bound problem.
There are classes of programs that do significant computation without talking to the network or accessing a file.
These are the CPU-bound programs, because the resource limiting the speed of your program is the CPU,
not the network or the file system.
"""


import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers_atr):
    for number in numbers_atr:
        cpu_bound(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
