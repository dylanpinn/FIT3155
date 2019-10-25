"""
FIT3155 - Lab 2

Question 3

Write a program to generate a random string of any stated length n
from a binary alphabet {H, T}, with the probability of character H
being p (and hence probability of T is 1 − p). Your program should
take n and p as arguments to write out a random string to a file

Dylan Pinn - 24160547
"""

from numpy.random import choice


def generate(n, p):
    string = "".join(choice(["H", "T"], n, p=[p, (1 - p)]))
    return string
