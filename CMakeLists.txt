cmake_minimum_required(VERSION 3.16)
project(TETHYS_Hydrodynamic_Simulation)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/lib")

enable_testing()

include_directories(src/)
include_directories(src/includes)

find_package(HDF5 REQUIRED COMPONENTS CXX)
include_directories(${HDF5_INCLUDE_DIRS})

find_package(GSL REQUIRED)
link_libraries(GSL::gsl GSL::gslcblas)

#set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wno-unused-parameter -O2")
set(CMAKE_CXX_FLAGS "-O2")
FIND_PACKAGE(OpenMP REQUIRED)
if(OPENMP_FOUND)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_C_FLAGS}")
endif()


add_executable(TEST src/RAFAELmain.cpp)


file(GLOB SRC_LIB_FILES src/*Lib.cpp)
add_library(tethys_library STATIC ${SRC_LIB_FILES})

target_link_libraries(TEST PUBLIC tethys_library)

target_include_directories(TEST PRIVATE ${HDF5_INCLUDE_DIRS})
target_link_libraries(TEST PRIVATE ${HDF5_CXX_LIBRARIES})

