#include <iostream>

bool is_prime(int n) {
  bool bl = true;
  for (int j=2; j<n; j++) {
    if (n%j == 0) {
      bl = false;
      break;
    }
  }
  return bl;
}

int main() {
  int n = 50000;
  int cnt = 0;
  for (int i=1; i<=n; i++) {
    if (is_prime(i)) cnt++;
  }
  std::cout << cnt << std::endl;
  return 0;
}
