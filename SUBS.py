#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


def find_substring_indices(string, substring):
    """
    Find all starting indices of occurrences of a substring within a string.
    """
    indices = []
    len_string = len(string)
    len_substring = len(substring)
    for i in range(len_string - len_substring + 1):
        if string[i : i + len_substring] == substring:
            indices.append(i + 1)
    return " ".join(map(str, indices))


def main():
    input_path = Path("data/rosalind_subs.txt")
    output_path = Path("output/rosalind_subs_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as f:
        string, substring = [line.strip() for line in f.read().splitlines()]

    output_str = find_substring_indices(string, substring)

    with open(output_path, "w") as f:
        f.write(output_str)

    print(output_str)
    print(f"Output written to {output_path}")


if __name__ == "__main__":
    main()

    input_string = "GATATATGCATATACTT"
    input_substring = "ATAT"

    print(find_substring_indices(input_string, input_substring))
