# CMake templates - external toolchain
As th name states this CMake example uses a (dummy) external toolchain
to process a set of input files and therefore make them usable for
compilation. The executable compiled just outputs 'Hello World!' on the
command line.

### Prerequisites
The project defines a CMakeLists.txt to control the build process. The
external toolchain is controlled by a helper script which is configured
by Cmake. The script invocation is encapsulated in a Cmake custom
command that is automatically executed by the main build target. As
additional target dependency a custom Cmake target is defined to deal
with deletion of the files created/processed by the external toolchain.

The resulting dependency cycle outlined:

1. Remove old processed files if exisiting
2. Process auxiliary files with external toolchain
3. Build CMake targets

### External toolchain
The external toolchain within this example is just a small python script
that removes '@' characters in the [auxiliary.h](auxiliary.h) header
file to make it usable within [main.cpp](main.cpp). This processing step
is just a surrogate for some real world application (e.g. using the
[protobuf](https://developers.google.com/protocol-buffers/) or
[odb](http://www.codesynthesis.com/products/odb/) compiler to create
support code for the project).
As a result we get a c++ header file (greeter.h) that will show up in
the CMake binary directory.

