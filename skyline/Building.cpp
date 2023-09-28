#include "Building.h"

void Building::setcoordinate(size_t l, size_t r, size_t h) { Left = l; Right = r; Height = h; }

size_t Building::getLeft() { return Left; }
size_t Building::getRight() { return Right; }
size_t Building::getHeight() { return Height; }