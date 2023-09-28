#ifndef SKYLINE_H
#define SKYLINE_H

#include<vector>
#include "Building.h"
using namespace std;


class Skyline {
    vector <Building> Buildings;
public:
    //  Skyline(); // an empty skyline
    void add(size_t l, size_t r, size_t h); // add a building with coordinates
    vector<pair<size_t, size_t> > getAsSequence(); // create the sequence
}; 
#endif