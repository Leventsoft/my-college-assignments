#include "shapes.h"
#include <iostream>

int main() {
    PlanarShape *planar[] = {
        new Circle(),
        new Square(),
        new Circle(4, 8),
        new Square(15, 16),
        new Circle(23, 42, 108),
        new Square(4, 8, 15)
    };

    int lengthOfPlanar = sizeof(planar) / sizeof(PlanarShape*);

    for (int i = 0; i < lengthOfPlanar; ++i)
        std::cout << "Circumference of " << i << "th planar shape is "
                  << planar[i]->circumference() << std::endl;

    VolumetricShape *volumetric[] = {
        new Sphere(),
        new Cube(),
        new Sphere(4, 8, 15),
        new Cube(16, 23, 42),
        new Sphere(16, 23, 42, 108),
        new Cube(4, 8, 15, 16)
    };

    int lengthOfVolumetric = sizeof(volumetric) / sizeof(VolumetricShape*);

    for (int i = 0; i < lengthOfVolumetric; ++i)
        std::cout << "Volume of " << i << "th volumetric shape is "
                  << volumetric[i]->volume() << std::endl;

    Shape **shapes;
    int lengthOfShapes = lengthOfPlanar + lengthOfVolumetric;
    shapes = new Shape*[lengthOfShapes];

    for (int i = 0; i < lengthOfPlanar; ++i)
        shapes[i] = planar[i];

    for (int i = 0, j = lengthOfPlanar; i < lengthOfVolumetric; ++i, ++j)
        shapes[j] = volumetric[i];

    for (int i = 0; i < lengthOfShapes; ++i)
        std::cout << "Area of " << i << "th shape is " << shapes[i]->area() << std::endl;

    for (int i = 0; i < lengthOfPlanar; ++i)
        delete planar[i];
    for (int i = 0; i < lengthOfVolumetric; ++i)
        delete volumetric[i];
    delete[] shapes;

    return 0;
}
