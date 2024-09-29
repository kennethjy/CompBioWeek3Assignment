possibilities = {'Stop': ['UAA', 'UAG', 'UGA'], 'M': ['AUG'], 'F': ['UUU', 'UUC'],
                 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                 'Y': ['UAU', 'UAC'], 'C': ['UGU', 'UGC'], 'W': ['UGG'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
                 'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                 'I': ['AUU', 'AUC', 'AUA'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
                 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'],
                 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG']}


def isValid(codons):
    for i in codons:
        if i not in possibilities:
            return False
    return True


def countRNACodons(rna):
    counts = {}
    for i in range(0, len(rna), 3):
        rnaCodon = rna[i:i+3]
        if rnaCodon in counts:
            counts[rnaCodon] += 1
        else:
            counts[rnaCodon] = 1
    print()
    print(f"mRNA = {rna}")
    for i in counts:
        print(f"{i} = {counts[i]}")


def recurse(codons, rna = ""):
    if len(codons) == 0:
        countRNACodons(rna)
    else:
        for i in possibilities[codons[0]]:
            recurse(codons[1:], rna + i)


codons = input("Input Amino acid = ")
while len(codons) > 3 or not isValid(codons):
    if len(codons) > 3:
        print("Maximum length is 3")
    else:
        print("Invalid codon(s) detected")
    codons = input("Input Amino acid = ")

recurse(codons)