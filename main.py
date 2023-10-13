from src import seq_complement
from src import check_primers
from src import mutation_position
from src import translation


# Функції для доступних опції
def check_primers_option():
    seq_f = input("Enter your Forward sequence: ").upper()
    seq_r = input("Enter your Reverse sequence: ").upper()
    check_primers.checkPrimers(seq_f, seq_r)


def seq_complement_option():
    seq = input("Enter the sequence: ").upper()
    res = seq_complement.getComplementSeq(seq)
    print(res)


def seq_reverse_complement_option():
    seq = input("Enter the sequence: ").upper()
    res = seq_complement.getComplementSeq(seq)
    print(res[::-1])


def find_mutation_position_option():
    seq1 = input("Enter the first sequence: ")
    seq2 = input("Enter the second sequence: ")
    res = mutation_position.getMutatedNucl(seq1, seq2)


def get_mrna_or_protein_option():
    option = int(input("To get mRNA, enter 1. To get protein, enter 2: "))
    if option == 1:
        res = translation.proteinDB(input("Enter your DNA sequence: "))
    elif option == 2:
        # Handle protein retrieval here
        pass


# Create a dictionary to map program numbers to their respective functions
program_options = {
    1: check_primers_option,
    2: seq_complement_option,
    3: seq_reverse_complement_option,
    4: find_mutation_position_option,
    5: get_mrna_or_protein_option,
}

while True:
    print("1 - Check your primers")
    print("2 - Seq_complement")
    print("3 - Seq_reverse_complement")
    print("4 - Find single mutation position")
    print("5 - Get mRNA/protein the sequence")
    print("6 - Check gene expression")
    print("7 - Create PCR project")
    print("8 - Go to pizda")

    numProgram = int(input("Choose the program (or enter 0 to exit): "))

    if numProgram == 0:
        break

    # Check if the chosen program number exists in the dictionary
    if numProgram in program_options:
        # Execute the corresponding function
        program_options[numProgram]()
    else:
        print("Invalid program number. Try again.")
