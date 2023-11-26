import argparse


def main():
    psr = argparse.ArgumentParser()
    psr.add_argument("arg1", help="positional argument, required")
    psr.add_argument("-a", "--alpha", help="basic format of optional argument")
    psr.add_argument("--default_value", default="Hello")
    psr.add_argument("--integer", type=float)
    psr.add_argument("--choice", choices=["hoge", "fuga", "piyo"])
    psr.add_argument("--args", nargs="*")
    args = psr.parse_args()

    print(args)


if __name__ == "__main__":
    main()
