import sys, time

def print_progress(text: str):
    sys.stderr.write("\r%s" % text)
    sys.stderr.flush()
    time.sleep(0.01)

for _ in range(0, 100):
    print_progress('progress: %d' % _)

print("\nFinish!!")
