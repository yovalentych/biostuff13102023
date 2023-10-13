from src import seq_complement
from src import check_primers
from src import mutation_position
from src import translation

print("1 - Check your primers (enter 1)")
print("2 - Seq_complement (enter 2)")
print("3 - Seq_reverse_complement (enter 3)")
print("4 - Find single mutation position (enter 4)")
print("5 - Get mRNA/protein the sequence (enter 5)")

numProgram = int(input("Chose the program: "))

if numProgram == 1:
    seq_f = input("Введіть свою Forward послідовність: ").upper()
    seq_r = input("Введіть свою Reverse послідовність: ").upper()

    check_primers.checkPrimers(seq_f, seq_r)
elif numProgram == 2:
    res = seq_complement.getComplementSeq(input("Enter seq: ").upper())
    print(res)
elif numProgram == 3:
    res = seq_complement.getComplementSeq(input("Enter seq: ").upper())
    print(res[::-1])
elif numProgram == 4:
    seq1 = input("Введіть першу послідовність: ")
    seq2 = input("Введіть другу послідовність: ")
    res = mutation_position.getMutatedNucl(seq1, seq2)
elif numProgram == 5:
    # print(5)
    # print("To get mRMA enter 51")
    # print("To get protein enter 52")
    # option = int(input("???: "))
    # if(option == 51):
    #     res = translation.proteinDB.get
    res = translation.proteinDB(input("Введіть будь-ласка свою ДНК послідовність: "))
else:
    print("Error. Try again")
