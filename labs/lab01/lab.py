# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    nums.sort()
    n = len(nums)

    mean = sum(nums) / n

    if n % 2 == 1:
        median = nums[n // 2] # odd length
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2 # even length
    
    return median <= mean


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    prefixes = [s[:i] for i in range(1, n + 1)]
    prefixes.reverse()
    return ''.join(prefixes)



# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    all_nums = []
    
    for num in ints:
        all_nums += list(range(num - n, num + n + 1))

    max_len = len(str(max(all_nums)))

    result = []
    for num in ints:
        exploded = [str(i).zfill(max_len) for i in range(num - n, num + n + 1)]
        result.append(' '.join(exploded))

    return result


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def last_chars(fh):
    results = ''
    for i in fh:
        i = i.rstrip('\n')
        if i:
            results += i[-1]

    return results


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    ...

def where_square(A):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    ...

def with_leftover(A):
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    ...
