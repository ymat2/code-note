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
    parser.add_argument("--vervose", default=1, type=int)
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    log_config(args.vervose)

    logger.info("function `twice()` started.")
    if type(args.input) != int:
        logger.warning("Input type in not integer!!")
    answer = twice(args.input)
    logger.info("function `twice()` ended.")
    print(answer)


def log_config(ll: int) -> None:
    from logging import basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL
    _log_levels = {
        -1: DEBUG,
        0: INFO,
        1: WARNING,
        2: ERROR,
        3: CRITICAL
    }
    basicConfig(
        format='%(levelname)s: %(message)s (%(filename)s)',
        level=_log_levels[ll],
        stream=sys.stderr
    )


def twice(i: int) -> int:
    i2 = i * 2
    return(i2)


if __name__ == "__main__":
    main()
