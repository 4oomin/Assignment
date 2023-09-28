#include "Skyline.h"


#include <algorithm>

void Skyline::add(size_t l, size_t r, size_t h) {
	Building tmp;
	tmp.setcoordinate(l, r, h);
	Buildings.push_back(tmp);
}

vector<pair<size_t, size_t> > Skyline::getAsSequence() {
	vector<pair<size_t, size_t> > skyline;
	size_t max_prev = 0, max_tmp = 0;
	sort(Buildings.begin(), Buildings.end());
	for (int i = 0; i <= 255; i++) {
		for (int j = 0; j < Buildings.size(); j++) {
			if (Buildings[j].getRight() < i) continue;
			if (Buildings[j].getLeft() > i) break;
			else {
				if (Buildings[j].getHeight() > max_tmp) max_tmp = Buildings[j].getHeight();
			}
		}
		if (max_tmp != max_prev) {
			if (max_tmp < max_prev) skyline.push_back({ i - 1,max_tmp });
			else skyline.push_back({ i,max_tmp });
		}
		max_prev = max_tmp;
		max_tmp = 0;
	}
	return skyline;
}