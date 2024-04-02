#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

class PayCalculator
{
public:
		PayCalculator() {
		}

		string calculate(string empleado) {
			vector<string> datos = split(empleado, '-');
			string r;
			switch (stoi(datos[0])) {
					case 1: r = PayM1(datos); break;
					case 2: r = PayM2(datos); break;
					case 3: r = PayM3(datos); break;
			}
			return r;
		}

		string PayM1(vector<string>& datos)
		{
				int total = stoi(datos[2]) * stoi(datos[3]);
				stringstream ss;
				ss << total;
				string totalstr = ss.str();    // Convertir int a string
				return datos[1] + totalstr;
		}

		string PayM2(vector<string>& datos)
		{
				int total = stoi(datos[2]) * stoi(datos[3]);
				stringstream ss;
				ss << total;
				string totalstr = ss.str();    // Convertir int a string
				return datos[1] + totalstr;
		}

		string PayM3(vector<string>& datos)
		{
				int total = stoi(datos[2]) * stoi(datos[3]);
				stringstream ss;
				ss << total;
				string totalstr = ss.str();    // Convertir int a string
				return datos[1] + totalstr;
		}

		vector<string> split(string str, char pattern) {
				int posInit = 0;
				int posFound = 0;
				string splitted;
				vector<string> results;

				while (posFound >= 0) {
						posFound = str.find(pattern, posInit);
						if (posFound == string::npos) {
								splitted = str.substr(posInit);
						} else {
								splitted = str.substr(posInit, posFound - posInit);
						}
						posInit = posFound + 1;
						results.push_back(splitted);
				}

				return results;
		}
};