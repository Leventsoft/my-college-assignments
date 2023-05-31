#include "shapes.h"
#include <iostream>
#include <cmath>

using namespace std;

// Circle implementation

Circle::Circle() : x(0), y(0), radius(1) {}

Circle::Circle(double radius) : x(0), y(0), radius(radius) {}

Circle::Circle(double x, double y) : x(x), y(y), radius(1) {}

Circle::Circle(double x, double y, double radius) : x(x), y(y), radius(radius) {}

double Circle::area() {
    return M_PI * radius * radius;
}

double Circle::circumference() {
    return 2 * M_PI * radius;
}

// Square implementation

Square::Square() : x(0), y(0), edgeLength(1) {}

Square::Square(double edgeLength) : x(0), y(0), edgeLength(edgeLength) {}

Square::Square(double x, double y) : x(x), y(y), edgeLength(1) {}

Square::Square(double x, double y, double edgeLength) : x(x), y(y), edgeLength(edgeLength) {}

double Square::area() {
    return edgeLength * edgeLength;
}

double Square::circumference() {
    return 4 * edgeLength;
}

// Cube implementation

Cube::Cube() : x(0), y(0), z(0), edgeLength(1) {}

Cube::Cube(double edgeLength) : x(0), y(0), z(0), edgeLength(edgeLength) {}

Cube::Cube(double x, double y, double z) : x(x), y(y), z(z), edgeLength(1) {}

Cube::Cube(double x, double y, double z, double edgeLength) : x(x), y(y), z(z), edgeLength(edgeLength) {}

double Cube::area() {
    return 6 * edgeLength * edgeLength;
}

double Cube::volume() {
    return edgeLength * edgeLength * edgeLength;
}

// Sphere implementation

Sphere::Sphere() : x(0), y(0), z(0), radius(1) {}

Sphere::Sphere(double radius) : x(0), y(0), z(0), radius(radius) {}

Sphere::Sphere(double x, double y, double z) : x(x), y(y), z(z), radius(1) {}

Sphere::Sphere(double x, double y, double z, double radius) : x(x), y(y), z(z), radius(radius) {}

double Sphere::area() {
    return 4 * M_PI * radius * radius;
}

double Sphere::volume() {
    return (4 / 3) * M_PI * radius * radius * radius;
}
