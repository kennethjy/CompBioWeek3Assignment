codon_table = {
    'AUG': ('Met', 'M'), 'UUU': ('Phe', 'F'), 'UUC': ('Phe', 'F'),
    'UUA': ('Leu', 'L'), 'UUG': ('Leu', 'L'), 'UCU': ('Ser', 'S'), 'UCC': ('Ser', 'S'),
    'UCA': ('Ser', 'S'), 'UCG': ('Ser', 'S'), 'UAU': ('Tyr', 'Y'), 'UAC': ('Tyr', 'Y'),
    'UGU': ('Cys', 'C'), 'UGC': ('Cys', 'C'), 'UGG': ('Trp', 'W'), 'CUU': ('Leu', 'L'),
    'CUC': ('Leu', 'L'), 'CUA': ('Leu', 'L'), 'CUG': ('Leu', 'L'), 'CCU': ('Pro', 'P'),
    'CCC': ('Pro', 'P'), 'CCA': ('Pro', 'P'), 'CCG': ('Pro', 'P'), 'CAU': ('His', 'H'),
    'CAC': ('His', 'H'), 'CAA': ('Gln', 'Q'), 'CAG': ('Gln', 'Q'), 'CGU': ('Arg', 'R'),
    'CGC': ('Arg', 'R'), 'CGA': ('Arg', 'R'), 'CGG': ('Arg', 'R'), 'AUU': ('Ile', 'I'),
    'AUC': ('Ile', 'I'), 'AUA': ('Ile', 'I'), 'GUU': ('Val', 'V'), 'GUC': ('Val', 'V'),
    'GUA': ('Val', 'V'), 'GUG': ('Val', 'V'), 'GCU': ('Ala', 'A'), 'GCC': ('Ala', 'A'),
    'GCA': ('Ala', 'A'), 'GCG': ('Ala', 'A'), 'GAU': ('Asp', 'D'), 'GAC': ('Asp', 'D'),
    'GAA': ('Glu', 'E'), 'GAG': ('Glu', 'E'), 'GGU': ('Gly', 'G'), 'GGC': ('Gly', 'G'),
    'GGA': ('Gly', 'G'), 'GGG': ('Gly', 'G'), 'UAA': ('Stop', None), 'UAG': ('Stop', None),
    'UGA': ('Stop', None), 'ACU': ('Thr', 'T'), 'ACC': ('Thr', 'T'), 'ACA': ('Thr', 'T'),
    'ACG': ('Thr', 'T'), 'AAU': ('Asn', 'N'), 'AAC': ('Asn', 'N'), 'AAA': ('Lys', 'K'),
    'AAG': ('Lys', 'K'), 'AGU': ('Ser', 'S'), 'AGC': ('Ser', 'S'), 'AGA': ('Arg', 'R'),
    'AGG': ('Arg', 'R')
}

def isValid(dna):
    if len(dna) % 3 != 0:
        return False
    for i in dna:
        if i not in "ATCG":
            return False
    return True


def complement(dna):
    comp = ""
    for i in dna:
        if i not in "ATGC":
            return "Invalid."
        if i == "A":
            comp += "T"
        if i == "T":
            comp += "A"
        if i == "G":
            comp += "C"
        if i == "C":
            comp += "G"

    return comp


def toMrna(dna):
    comp = complement(dna)
    if comp != "Invalid.":
        return "".join(["U" if i == "T" else i for i in comp])
    else:
        return "Invalid."


def toAminoAcid(dna):
    mrna = toMrna(dna)
    aminos = []
    if mrna != "Invalid.":
        for i in range(0, len(mrna), 3):
            codon = codon_table[mrna[i: i + 3]]
            if codon[0] == "Stop":
                print("Stop Codon detected")
                break
            else:
                aminos.append(f"{codon[0]} ({codon[1]})")
        return " - ".join(aminos)
    else:
        return "Invalid."


def showStepsToAminoAcid(dna):
    print(f"Complement = {complement(dna)}")
    print(f"mRNA = {toMrna(dna)}")
    print(f"Amino acid = {toAminoAcid(dna)}")


dna = input("Input DNA = ").strip()
while not isValid(dna):
    if len(dna) % 3 != 0:
        print("Length has to be a multiple of 3")
    else:
        print("Invalid Characters Detected")
    dna = input("Input DNA = ").strip()

print()
showStepsToAminoAcid(dna)
