def proteinDB(dna_seq):
    def getTranscription(dna_seq):
        rna_seq = ""

        for nucl in dna_seq:
            if nucl == "G":
                nucl = "C"
            elif nucl == "C":
                nucl = "G"
            elif nucl == "T":
                nucl = "A"
            elif nucl == "A":
                nucl = "U"

            rna_seq += nucl

        return rna_seq

    def getTranslation(rna_seq):
        genetic_code = {
            "UUU": "F",
            "UUC": "F",
            "UUA": "L",
            "UUG": "L",
            "UCU": "S",
            "UCC": "S",
            "UCA": "S",
            "UCG": "S",
            "UAU": "Y",
            "UAC": "Y",
            "UAA": "STOP",
            "UAG": "STOP",
            "UGU": "C",
            "UGC": "C",
            "UGA": "STOP",
            "UGG": "W",
            "CUU": "L",
            "CUC": "L",
            "CUA": "L",
            "CUG": "L",
            "CCU": "P",
            "CCC": "P",
            "CCA": "P",
            "CCG": "P",
            "CAU": "H",
            "CAC": "H",
            "CAA": "Q",
            "CAG": "Q",
            "CGU": "R",
            "CGC": "R",
            "CGA": "R",
            "CGG": "R",
            "AUU": "I",
            "AUC": "I",
            "AUA": "I",
            "AUG": "M",
            "ACU": "T",
            "ACC": "T",
            "ACA": "T",
            "ACG": "T",
            "AAU": "N",
            "AAC": "N",
            "AAA": "K",
            "AAG": "K",
            "AGU": "S",
            "AGC": "S",
            "AGA": "R",
            "AGG": "R",
            "GUU": "V",
            "GUC": "V",
            "GUA": "V",
            "GUG": "V",
            "GCU": "A",
            "GCC": "A",
            "GCA": "A",
            "GCG": "A",
            "GAU": "D",
            "GAC": "D",
            "GAA": "E",
            "GAG": "E",
            "GGU": "G",
            "GGC": "G",
            "GGA": "G",
            "GGG": "G",
        }
        protein = ""
        n = 0
        while n < len(rna_seq):
            codon = rna_seq[n : n + 3]
            aminoacid = genetic_code.get(codon, "")
            if aminoacid == "STOP":
                break
            protein += aminoacid
            n += 3
        return protein

    rna_seq = getTranscription(dna_seq)
    print(f"RNA: {rna_seq}")
    protein = getTranslation(rna_seq)
    print(f"Protein: {protein}")
