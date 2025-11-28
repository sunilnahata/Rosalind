#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) 
in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several 
possible consensus strings exist, then you may return any one of them.)
"""

from pathlib import Path
from pprint import pprint
from GC import parse_fasta

nucleotides = ("A", "C", "G", "T")


def profile(sequences):
    """
    Generate a profile matrix counting nucleotide occurrences at each position.
    """
    length = len(sequences[0])
    profile_matrix = {nuc: [0] * length for nuc in nucleotides}
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile_matrix[nucleotide][i] += 1
    return profile_matrix


def consensus(profile_matrix):
    """
    Return the consensus string with the most frequent nucleotide at each
    position.
    """
    consensus_string = ""
    length = len(next(iter(profile_matrix.values())))
    for i in range(length):
        max_nucleotide_count = -1
        max_occuring_nucleotide = ""
        for nucleotide in nucleotides:
            if profile_matrix[nucleotide][i] > max_nucleotide_count:
                max_nucleotide_count = profile_matrix[nucleotide][i]
                max_occuring_nucleotide = nucleotide
        consensus_string += max_occuring_nucleotide
    return consensus_string


def main():
    input_path = Path("data/rosalind_cons.txt")
    output_path = Path("output/rosalind_cons_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert FASTA dict to list of sequences
    sequences = list(parse_fasta(input_path).values())

    profile_matrix = profile(sequences)
    consensus_string = consensus(profile_matrix)

    with open(output_path, "w") as f:
        f.write(consensus_string + "\n")
        for nuc in nucleotides:
            f.write(f"{nuc}: {' '.join(map(str, profile_matrix[nuc]))}\n")
    print(f"Output written to {output_path}")

    print(consensus_string)
    for nuc in nucleotides:
        print(f"{nuc}: {' '.join(map(str, profile_matrix[nuc]))}")


if __name__ == "__main__":
    main()
