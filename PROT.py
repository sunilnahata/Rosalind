#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path

def translate_rna_to_protein(rna_sequence):
    """
    Translate an RNA sequence into a protein string using the codon table.
    """
    codon_table = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }
    protein_sequence = ""
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if codon_table.get(codon) == "Stop":
            break
        protein_sequence += codon_table.get(codon)
    return protein_sequence

def main():
    input_path = Path("data/rosalind_prot.txt")
    output_path = Path("output/rosalind_prot_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(input_path, "r") as f:
        rna_sequence = f.readline().strip()
        protein_sequence = translate_rna_to_protein(rna_sequence)

    with open(output_path, "w") as f:
        f.write(f"{protein_sequence}\n")
        print(f"Protein sequence written to {output_path}")


if __name__ == "__main__":
    main()
    # rna_sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    # protein_sequence = translate_rna_to_protein(rna_sequence)
    # print(protein_sequence)