from functools import reduce
import string
import math
import pandas as pd
import numpy as np


def assertEqual(expected, actual) -> string:
    if (expected != actual):
        print ( f"\tFAIL: expected: {expected} but got: {actual}")
    else:
        print  ("\tPass")


def aggrigate_func(series: pd.Series):
    return reduce (lambda a, b: base60_subtraction(a,b), series)


def test_agg_func():
    print("Test Agg Func")
    series1 = pd.Series(np.array([1000,1015,1145,1200]))
    assertEqual(0.5, aggrigate_func(series=series1))

def test_base_60_subtraction():
    print("Base 60 Subtraction")
    assertEqual(0.25, base60_subtraction(1000,1015))
    assertEqual(0.5, base60_subtraction(1015,1045))
    assertEqual(0.75, base60_subtraction(1015,1100))
    assertEqual( 1.0, base60_subtraction(1000,1100))
    assertEqual(1.25, base60_subtraction(1015,1130))


def base60_subtraction(a: int, b:int) -> float:
    aTens = math.floor(a/100)
    aSixtys = a%100
    bTens = math.floor(b/100)
    bSixtys = b%100

    borrowing = bSixtys < aSixtys

    if borrowing:
        bTens = bTens -1
        bSixtys = bSixtys + 60

    return (bTens - aTens) + (bSixtys - aSixtys)/60

if __name__ == '__main__':
    test_base_60_subtraction()
    test_agg_func()
