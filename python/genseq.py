import argparse
import random
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    parser.add_argument("-n", "--numseq", type = int, dest = "number_of_seq", default = 10)
    parser.add_argument("-l", "--lenseq", type = int, dest = "length_of_seq")
    args = parser.parse_args()

    outseq = generate_random_seq(n = args.number_of_seq, l = args.length_of_seq)
    write_fasta(outseq, args.output)


class Seq:
    def __init__(self, hdr, seq) -> None:
        self.header = hdr
        self.sequence = seq

    def to_complement(self):
        complementary_nucs = {
            "A" : "T",
            "T" : "A",
            "G" : "C",
            "C" : "G"
        }
        self.sequence = "".join([complementary_nucs[base] for base in self.sequence])


def generate_random_seq(n: int, l: int) -> list:
    if not l:
        l = random.randrange(30, 40)
    random_seq = []
    for i in range(n):
        i = i + 1
        hdr = "Seq_" + str(i)
        seq = "".join(random.choices(["A", "T", "G", "C"], k = l))
        random_seq.append(Seq(hdr = hdr, seq = seq))
    return random_seq


def write_fasta(seqs: list, outfile: Path) -> None:
    with open(outfile, "w") as f:
        for seq in seqs:
            seq.to_complement()
            f.write(">" + seq.header + "\n")
            f.write(seq.sequence + "\n")


if __name__ == "__main__":
    main()
