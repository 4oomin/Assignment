#ifndef BUILDING_H
#define BUILDING_H


class Building {
	size_t Left;
	size_t Right;
	size_t Height;
public:
	bool operator <(Building& building) {
		return this->Left < building.Left;
	}

	void setcoordinate(size_t l, size_t r, size_t h); 

	size_t getLeft(); 
	size_t getRight(); 
	size_t getHeight(); 

};

#endif
