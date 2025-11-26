#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given: Three positive integers k, m, and n, representing a population 
containing k+m+n organisms: k individuals are homozygous dominant for a factor, 
m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will 
produce an individual possessing a dominant allele (and thus displaying the 
dominant phenotype). Assume that any two organisms can mate.
"""
from pathlib import Path


def dominant_allele_probability(k, m, n):
    """
    Calculate the probability that two randomly selected mating organisms
    will produce an individual possessing a dominant allele.
    """
    total = k + m + n
    p_AA_AA = (k / total) * ((k - 1) / (total - 1))
    p_AA_Aa = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    p_AA_aa = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    p_Aa_Aa = (m / total) * ((m - 1) / (total - 1))
    p_Aa_aa = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))

    prob_dominant = (
        p_AA_AA * 1.0 + p_AA_Aa * 1.0 + p_AA_aa * 1.0 + p_Aa_Aa * 0.75 + p_Aa_aa * 0.5
    )

    return prob_dominant


def main():
    input_path = Path("data/rosalind_iprb.txt")
    output_path = Path("output/rosalind_iprb_output.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(input_path, "r") as f:
        k, m, n = map(int, f.readline().strip().split())
        prob_dominant = dominant_allele_probability(k, m, n)

    with open(output_path, "w") as f:
        f.write(f"{prob_dominant:.5f}\n")
        print(f"Probability of {prob_dominant:.5f} written to {output_path}")


if __name__ == "__main__":
    main()


# ## Alernative implementation using combinations from math module
# from math import comb

# def dominant_allele_probability(k, m, n):
#     total = k + m + n
#     total_pairs = comb(total, 2)

#     prob_recessive = (
#         comb(n, 2) +
#         comb(m, 2) * 0.25 +
#         m * n * 0.5
#     ) / total_pairs

#     return 1 - prob_recessive 