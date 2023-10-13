def getComplementSeq(seqForComplement):
    complementary = str()
    for char in seqForComplement:
        if char == "C":
            char = "G"
        elif char == "G":
            char = "C"
        elif char == "T":
            char = "A"
        elif char == "A":
            char = "T"
        complementary += char
    return complementary
