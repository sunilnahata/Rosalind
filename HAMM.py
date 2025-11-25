#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculating the Hamming distance between two given sequences.
"""

from pathlib import Path


def hamming_distance(sequence1, sequence2):
    """
    Calculate and return the Hamming distance between two given sequences.
    """
    return sum(a != b for a, b in zip(sequence1, sequence2))


def main():
    input_path = Path("data/rosalind_hamm.txt")
    output_path = Path("output/rosalind_hamm_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(input_path, "r") as f:
        seq1 = f.readline().strip()
        seq2 = f.readline().strip()
        distance = hamming_distance(seq1, seq2)

    with open("output/rosalind_hamm_output.txt", "w") as f:
        f.write(f"{distance}")

    print(f"Hamming distance: {distance}")
    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
