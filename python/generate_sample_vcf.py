import argparse
import random
from pathlib import Path
from string import ascii_uppercase


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="sample.vcf")
    parser.add_argument("--nchr", type=int, help="Number of chromosomes", default=1)
    parser.add_argument("--nfam", type=int, help="Number of families", default=1)
    parser.add_argument("--nindv_per_fam", type=int, help="Number of individuals per family", default=5)
    parser.add_argument("--nsite_per_chrom", type=int, help="Number of sites per chromosome", default=10)
    parser.add_argument("--seed", type=int, help="Random seed", default=12345)
    args = parser.parse_args()
    random.seed(args.seed)
    generate_sample_vcf(file=args.output, nchr=args.nchr, nfam=args.nfam, nindv=args.nindv_per_fam, nsite=args.nsite_per_chrom)


def generate_sample_vcf(file: Path, nchr: int, nfam: int, nindv: int, nsite: int) -> None:
    _header = [
        '##fileformat=VCFv4.2',
        '##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">',
        '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">'
    ]
    indvs = ["GRP"+ascii_uppercase[i]+"_"+str(j+1) for i in range(nfam) for j in range(nindv)]
    _cols = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
    _cols += indvs
    with open(file, "w") as f:
        for l in _header:
            f.write(l+"\n")
        f.write("\t".join(_cols)+"\n")
        for c in range(nchr):
            _chrom = "chr"+str(c+1)
            for s in range(nsite):
                _pos = str(100+10*s)
                rec = generate_record(nsample = len(indvs))
                rec = [_chrom, _pos] + rec
                f.write("\t".join(rec)+"\n")


def generate_record(nsample: int) -> list:
    _id = '.'
    _ref, _alt = generate_random_variant_pair(max_seq_len=5)
    _qual = '256'
    _filter = '.'
    _dp = 'DP=35'
    _format = 'GT'
    records = [random.choice(["0/0", "0/1", "1/1"]) for _ in range(nsample)]
    records = [_id, _ref, _alt, _qual, _filter, _dp, _format] + records
    return records


def generate_random_variant(max_seq_len: int = 5) -> str:
    _gts = ["A", "T", "G", "C"]
    rand = random.random()
    if rand < 0.8:
        seq_len = 1
    elif rand < 0.9:
        seq_len = 0
    else:
        seq_len = random.randint(2, max_seq_len)
    if seq_len == 0:
        sequence = "."
    else:
        sequence = ''.join(random.choices(_gts, k=seq_len))
    return sequence


def generate_random_variant_pair(max_seq_len: int = 5) -> tuple:
    _ref = generate_random_variant(max_seq_len = max_seq_len)
    while True:
        _alt = generate_random_variant(max_seq_len = max_seq_len)
        if _ref != _alt:
            break
    return _ref, _alt


if __name__ == "__main__":
    main()
