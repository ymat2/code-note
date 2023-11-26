#include <iostream>
#include <cmath>

bool is_prime(int n) {
    // 2未満の数は素数ではない
    if (n < 2) {
        return false;
    }

    // 2は素数
    if (n == 2) {
        return true;
    }

    // 2以外の偶数は素数ではない
    if (n % 2 == 0) {
        return false;
    }

    // 3以上の奇数で割り切れるかどうかを調べる
    // 2と3以外の素数は6の倍数の前後にしか存在しない性質を利用している
    for (int i = 3; i <= std::sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }

    // どの数でも割り切れなかった場合は素数
    return true;
}

int main() {
    // テスト例
    int number;
    std::cout << "整数を入力してください: ";
    std::cin >> number;

    if (is_prime(number)) {
        std::cout << number << " は素数です。\n";
    } else {
        std::cout << number << " は素数ではありません。\n";
    }

    return 0;
}
