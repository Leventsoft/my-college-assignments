#ifndef SHAPES_H
#define SHAPES_H

#include <iostream>
#include <cmath>

class Shape {
public:
    virtual double area() = 0;
};

class PlanarShape : public Shape {
public:
    virtual double circumference() = 0;
};

class Circle : public PlanarShape {
private:
    double x, y, radius;

public:
    Circle();
    Circle(double radius);
    Circle(double x, double y);
    Circle(double x, double y, double radius);
    double area();
    double circumference();
};

class Square : public PlanarShape {
private:
    double x, y, edgeLength;

public:
    Square();
    Square(double edgeLength);
    Square(double x, double y);
    Square(double x, double y, double edgeLength);
    double area();
    double circumference();
};

class VolumetricShape : public Shape {
public:
    virtual double volume() = 0;
};

class Cube : public VolumetricShape {
private:
    double x, y, z, edgeLength;

public:
    Cube();
    Cube(double edgeLength);
    Cube(double x, double y, double z);
    Cube(double x, double y, double z, double edgeLength);
    double area();
    double volume();
};

class Sphere : public VolumetricShape {
private:
    double x, y, z, radius;

public:
    Sphere();
    Sphere(double radius);
    Sphere(double x, double y, double z);
    Sphere(double x, double y, double z, double radius);
    double area();
    double volume();
};

#endif // SHAPES_H
