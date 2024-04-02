#include "FileReader.h"
#include "PayCalculator.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  // Read file
  FileReader fileReader = FileReader();
  vector<string> employees = fileReader.readFile();

  // Calculate pay for every employee coming from the file
  PayCalculator calculator = PayCalculator();
  for (auto &employee : employees) {
    // Show result in console
    string result = calculator.calculate(employee);
    cout << result << endl;
  }

  return 0;
}
