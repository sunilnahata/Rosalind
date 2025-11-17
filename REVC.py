#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Complementing a DNA strand.
"""
from pathlib import Path


def complement_dna(dna_sequence):
    """
    Returns the complementary DNA strand for a given DNA sequence.
    """
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in dna_sequence)


def main():
    input_path = Path("data/rosalind_revc.txt")
    output_path = Path("output/rosalind_revc_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as f:
        dna_sequence = f.read().strip()
        rev_comp_sequence = complement_dna(dna_sequence)[::-1]

    with open(output_path, "w") as f:
        f.write(f"{rev_comp_sequence}\n")

    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
