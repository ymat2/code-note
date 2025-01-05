import argparse
import gzip

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
args = parser.parse_args()

if args.input.lower().endswith(".gz"):
    handler = gzip.open
else:
    handler = open

with handler(args.input, 'rt') as f:
    for line in f:
        print(line.rstrip("\n"))
