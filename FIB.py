#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rabbits and Recurrence Relations
"""
from pathlib import Path


def fib_rabbits(n, k):
    """
    Calculate the number of rabbit pairs present after n months,
    given that each pair of rabbits produces k pairs of offspring
    starting from their second month of life.

    n : The number of months.
    k : The number of pairs produced by each pair of rabbits.

    Returns:
    int: The total number of rabbit pairs after n months.
    """
    if n == 1 or n == 2:
        return 1
    else:
        previous, current = 1, 1
        for _ in range(3, n + 1):
            next_value = current + k * previous
            previous, current = current, next_value
        return current


def main():
    input_path = Path("data/rosalind_fib.txt")
    output_path = Path("output/rosalind_fib_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("r") as file:
        n, k = map(int, file.read().strip().split())
        result = fib_rabbits(n, k)

    with output_path.open("w") as file:
        file.write(f"{result}\n")

    print(f"Results for n={n}, k={k}: {result}")
    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
    # n = 5
    # k = 3
    # print(fib_rabbits(n, k))  
