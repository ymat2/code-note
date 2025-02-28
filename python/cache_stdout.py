import sys, time

def print_progress(text: str):
    sys.stdout.write("\r%s" % text)
    sys.stdout.flush()
    time.sleep(0.01)

for _ in range(0, 100):
    print_progress('progress: %d' % _)
print("\nFinish!!")
