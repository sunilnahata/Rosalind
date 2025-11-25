#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculating GC Content in a set of DNA sequences and returning the ID of the
string having the highest GC-content, followed by the GC-content of that string.
"""

from pathlib import Path


def gc_content(dna_sequence):
    """
    Calculates the GC content percentage in a given DNA sequence.
    """
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    total_count = len(dna_sequence)
    return (gc_count / total_count) * 100


def parse_fasta(input_path):
    """
    Parses the data in fasta format from the input file and returns a
    dictionary mapping sequence identifiers to sequences.
    """
    sequences = {}
    identifier = ""
    with open(input_path) as f:
        for line in f:
            if line[0] == ">":
                identifier = line[1:].strip()
                sequences[identifier] = ""
            else:
                sequences[identifier] += line.strip()

    return sequences


def find_highest_gc_content(sequences):
    """
    Find highest GC content among the given sequences.
    """
    highest_gc_content = 0.0
    highest_gc_seq_id = ""
    for sequence_id, sequence in sequences.items():
        gc_percent = gc_content(sequence)
        if gc_percent > highest_gc_content:
            highest_gc_content = gc_percent
            highest_gc_seq_id = sequence_id
    return highest_gc_seq_id, highest_gc_content


def main():
    input_path = Path("data/rosalind_gc.txt")
    output_path = Path("output/rosalind_gc_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    sequences = parse_fasta(input_path)
    highest_gc_seq_id, highest_gc_content = find_highest_gc_content(sequences)

    with open(output_path, "w") as f:
        f.write(f"{highest_gc_seq_id}\n{highest_gc_content:.6f}\n")

    print(f"{highest_gc_seq_id}\n{highest_gc_content:.6f}\n")
    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
