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
    args = parser.parse_args()
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
    _gts = ["A", "T", "G", "C"]
    _id = '.'
    _ref, _alt = random.sample(_gts, 2)
    _qual = '256'
    _filter = '.'
    _dp = 'DP=35'
    _format = 'GT'
    records = [random.choice(["0/0", "0/1", "1/1"]) for _ in range(nsample)]
    records = [_id, _ref, _alt, _qual, _filter, _dp, _format] + records
    return records


if __name__ == "__main__":
    main()
