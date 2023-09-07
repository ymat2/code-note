#include<iostream>

int main(){
  std::vector<int> vec{0,0,0};
  std::cout << vec << std::endl;
  vec[2] = vec[1] + 1;
  std::cout << vec << std::endl;
  vec[1] = vec[0] + 1;
  std::cout << vec << std::endl;

  return 0;
}
