project(kalman)

cmake_minimum_required (VERSION 3.5)

add_definitions(-std=c++0x)

set(sources
        src/kalman_filter.cpp
        src/main.cpp
        src/tracking.cpp)

add_executable(kalman ${sources})
