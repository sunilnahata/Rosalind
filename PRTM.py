#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculate and return the total weight of a protein.
"""
from pathlib import Path


mass_table = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333,
}


def calculate_protein_weight(protein_sequence):
    """
    Given: A protein string P of length at most 1000 aa.
    Return: The total weight of P.
    """
    total_weight = 0.0
    for amino_acid in protein_sequence:
        total_weight += mass_table.get(amino_acid)
    return total_weight


def main():
    input_path = Path("data/rosalind_prtm.txt")
    output_path = Path("output/rosalind_prtm_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as f:
        protein_sequence = f.read().strip()
        result = calculate_protein_weight(protein_sequence)

    with open(output_path, "w") as f:
        f.write(f"{result:.3f}\n")
        print(f"Total weight of the protein: {result:.3f}")
        print(f"Result written to {output_path}")


if __name__ == "__main__":
    main()
