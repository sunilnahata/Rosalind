#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Counting Nucleotides in a DNA sequence.
"""

from pathlib import Path


def count_nucleotides(dna_sequence):
    """
    Counts the occurences of each nucleotide in a given DNA sequence.
    """
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in dna_sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    return counts


def main():
    input_path = Path("data/rosalind_dna.txt")
    output_path = Path("output/rosalind_dna_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as f:
        dna_sequence = f.read().strip()
        counts = count_nucleotides(dna_sequence)

    with open(output_path, "w") as f:
        f.write(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}\n")

    print(f"A: {counts['A']}, C: {counts['C']}, G: {counts['G']}, T: {counts['T']}")
    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
