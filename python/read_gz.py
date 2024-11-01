import gzip

file_path = "test/sample.tsv.gz"

with gzip.open(file_path, 'rt') as f:
    for line in f:
        print(line.rstrip("\n"))
