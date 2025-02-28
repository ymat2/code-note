"""
logging モジュールを使ったログレベルのコントロール
ここでは、Info 以上のログを標準エラー出力にするログを自前で設定する。
参考:
- https://qiita.com/smats-rd/items/c5f4345aca3a452041c7
- https://qiita.com/amedama/items/b856b2f30c2f38665701
あんまり理解できてない。。。
"""

import argparse
import sys
from logging import getLogger


logger = getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", default=0, type=int,
                        help="Set verbosity level (2:DEBUG, 1:INFO, 0:WARNING, -1:ERROR, -2:CRITICAL)")
    parser.add_argument("-i", "--input", type=int)
    args = parser.parse_args()

    log_config(args.verbose)

    logger.info("function `twice()` started.")
    if args.input < 10:
        msg = ["Input number is less than 10."]
        msg.append("Please input number larger than 10.")
        logger.warning("\n".join(msg))
    answer = twice(args.input)
    logger.info("function `twice()` ended.")
    print(answer)


def log_config(ll: int) -> None:
    from logging import basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL
    _log_levels = {
        2: DEBUG,
        1: INFO,
        0: WARNING,
        -1: ERROR,
        -2: CRITICAL
    }
    basicConfig(
        format='%(levelname)s: %(message)s (%(filename)s)',
        level=_log_levels.get(ll),
        stream=sys.stderr
    )


def twice(i: int) -> int:
    i2 = i * 2
    return(i2)


if __name__ == "__main__":
    main()
