#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

int main() {
  std::ifstream file("input.txt");
  if (!file) { return 1; }

  std::vector<std::vector<int>> nums;
  std::string line;
  while (std::getline(file, line)) {
    std::istringstream iss(line);
    std::vector<int> row;
    int x;
    while (iss >> x) { row.push_back(x); }
    nums.push_back(row);
  }
  file.close();

  int res1 = 0, res2 = 0;
  for (const auto& xs: nums) {
    int pd = 0;
    bool safe = true;
    for (size_t i = 0; i < xs.size() - 1; ++i) {
      int d = xs[i] - xs[i+1];
      if ((pd && pd * d <= 0) || !d || d*d > 9) { 
        safe = false;
        break; 
      }
      pd = d;
    }
    for (size_t j = 0; j < xs.size(); ++j) {
      int pd = 0;
      bool safe = true;
      std::vector<int> ys = xs;
      ys.erase(ys.begin() + j);

      for (size_t i = 0; i < ys.size() - 1; ++i) {
        int d = ys[i] - ys[i+1];
        if ((pd && pd * d <= 0) || !d || d*d > 9) { 
          safe = false;
          break; 
        }
        pd = d;
      }
      if (safe) {
        res2 += 1;
        break;
      }
    }
    res1 += safe;
  }

  printf("Part 1: %d\n", res1);
  printf("Part 2: %d\n", res2);
}
