"""
calculator.py
Calculator library containing basic math operations.
"""
from typing import Union


def add(first_term: Union[float, int], second_term: Union[float, int]) -> Union[float, int]:
    return first_term + second_term


def subtract(first_term: Union[float, int], second_term: Union[float, int]) -> Union[float, int]:
    return first_term - second_term


def multiply(first_term: Union[float, int], second_term: Union[float, int]) -> Union[float, int]:
    return first_term * second_term
