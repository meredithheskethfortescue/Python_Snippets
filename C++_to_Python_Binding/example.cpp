/*
Minimal example of a C++ to Python Binding using pybind11
Original code available at https://pybind11.readthedocs.io/en/latest/basics.html#compiling-the-test-cases

Compiler flags:
c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`
*/

#include <pybind11/pybind11.h>
namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers",
      py::arg("i"), py::arg("j"));

    m.attr("the_answer") = 42;
    py::object world = py::cast("World");
    m.attr("hello") = world;
}
