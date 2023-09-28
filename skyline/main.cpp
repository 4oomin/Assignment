#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cctype>

#include "Skyline.h"
#include "Building.h"

using namespace std;

int main() {
	size_t l, r, h;
	string input;
	string str;
	string tmp;
	int cnt = 0;
	Skyline skyline;

	cout << "입력: ";
	getline(cin,input);

	for (int i = 0; i < input.length(); ++i)
	{
		if (isspace(input[i]) ==0)
		{
			tmp += input[i];
		}
	}

	for (int i = 0; i < tmp.length(); i++) {
		if (tmp[i] != '[' && tmp[i] != ']' && tmp[i] != ',') {
			str += tmp[i];
		}
		else {
			if (str == "") continue;
			int m = stoi(str);
			size_t n = (size_t)m;
			str = "";
			if (cnt == 0) {
				l = n;
			}
			if (cnt == 1) {
				r = n;
			}
			if (cnt == 2) {
				h = n;
			}
			++cnt;
			if (cnt == 3) {
				skyline.add(l, r, h);
				cnt = 0;
			}

		}
	}
	cout << endl;



	vector<pair<size_t, size_t> > output;

	output = skyline.getAsSequence();

	cout << "출력: ";
	for (int i = 0; i < output.size(); i++) cout << "[" << output[i].first << "," << output[i].second << "] ";
	cout << endl;

	return 0;
}