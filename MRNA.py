#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

codon_table = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def codon_frequencies():
    """
    Calculate the frequency of each codon in the given RNA sequence.
    """
    frequency = {}
    for codon, amino_acid in codon_table.items():
        frequency[amino_acid] = frequency.get(amino_acid, 0) + 1
    return frequency


def possible_rna_strings(protein_sequence):
    """
    Calculate the number of different RNA sequences that can translate into the
    given protein sequence.
    """
    mod = 1_000_000
    freq = codon_frequencies()
    total = freq["Stop"]
    for amino_acid in protein_sequence:
        total = (total * freq[amino_acid]) % mod
    return total


def main():
    input_path = Path("data/rosalind_mrna.txt")
    output_path = Path("output/rosalind_mrna_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as f:
        protein_sequence = f.read().strip()

    result = possible_rna_strings(protein_sequence)

    with open(output_path, "w") as f:
        f.write(str(result))

    print(result)
    print(f"Output written to {output_path}")


if __name__ == "__main__":
    main()
    # print(possible_rna_strings("MA"))

"""
Another way to create codon table

bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
"""