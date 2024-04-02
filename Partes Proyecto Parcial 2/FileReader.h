#include "fstream"
#include "iostream"
#include "string"
#include "vector"

using namespace std;

class FileReader {
public:
  vector<string> readFile();
};

vector<string> FileReader::readFile() {
  vector<string> info;
  ifstream file;

  string fileName = "";

  cout << "Ingrese el nombre del archivo" << endl;
  cin >> fileName;

  file.open(fileName);
  bool emptyFile = !file;

  while (fileName == "" || emptyFile) {
    cout << "Ingrese un nombre válido..." << endl;
    cin >> fileName;
    file.open(fileName);
    emptyFile = !file;
  }

  string text;
  while (getline(file, text)) {
    info.push_back(text);
  }

  return info;
}
