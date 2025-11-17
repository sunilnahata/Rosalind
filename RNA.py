#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Transcribing DNA to RNA.
"""

from pathlib import Path


def transcribe_dna_to_rna(dna_sequence):
    """
    Transcribes a given DNA sequence into an RNA sequence by replacing
    all occurrences of Thymine (T) with Uracil (U).
    """
    return dna_sequence.replace("T", "U")


def main():
    input_path = Path("data/rosalind_rna.txt")
    output_path = Path("output/rosalind_rna_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as f:
        dna_sequence = f.read().strip()
        rna_sequence = transcribe_dna_to_rna(dna_sequence)

    with open(output_path, "w") as f:
        f.write(f"{rna_sequence}\n")

    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
