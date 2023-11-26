import argparse
from Bio.Seq import Seq


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--cds")
  parser.add_argument("-a", "--aa")
  args = parser.parse_args()

  cds_seq = fasta2dict(args.cds)
  aa_seq = dict()
  for gn, seq in cds_seq.items():
    seq = Seq(seq)
    seq = seq.translate(stop_symbol="*")
    aa_seq[gn] = str(seq)

  with open(args.aa, "w") as f:
    for gn, seq in aa_seq.items():
      f.write(gn+"\n"+seq+"\n")


def fasta2dict(path):
  seq_dict = dict()
  with open(path) as f:
    tmp_header = ""
    for line in f:
      if line[0] == ">":
        tmp_header = line.rstrip("\n")[1:]
        seq_dict[tmp_header] = ""
      else:
        seq_dict[tmp_header] += line.rstrip("\n")
  return seq_dict


def sample():
  from Bio.Seq import Seq

  sample_cds = "ATGGTCTTTGAAAGGTGTGAGTTGGCCAGAACTCTGAAATAG"
  sample_cds = Seq(sample_cds)  # convert string to Seq class
  sample_aa = sample_cds.translate(stop_symbol="*")
  sample_aa = str(sample_aa)  # convert Seq class to string for printing

  print(sample_aa)
  # MVFERCELARTLK*


if __name__ == "__main__":
  main()
