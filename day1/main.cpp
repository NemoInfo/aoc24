#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

int main() {
  std::ifstream file("input.txt");
  if (!file) { return 1; }

  std::vector<int> l1, l2;
  std::string line;
  int f1[100000] = {}, f2[100000] = {};
  while (std::getline(file, line)) {
    std::istringstream iss(line);
    int a, b;
    iss >> a >> b;
    f1[a] += 1, f2[b] += 1;
    l1.push_back(a), l2.push_back(b);
  }
  file.close();

  std::sort(l1.begin(), l1.end());
  std::sort(l2.begin(), l2.end());

  int res1 = 0, res2 = 0;
  for (size_t i = 0; i < l1.size(); ++i) {
    res1 += std::abs(l1[i] - l2[i]);
    res2 += l1[i] * f1[l1[i]] * f2[l1[i]];
    f1[l1[i]] = 0;
  }

  printf("Part 1: %d\n", res1);
  printf("Part 2: %d\n", res2);
}
