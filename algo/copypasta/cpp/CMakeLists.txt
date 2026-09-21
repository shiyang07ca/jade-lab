cmake_minimum_required(VERSION 3.23)
project(copypasta_cpp LANGUAGES CXX)

file(GLOB COPYPASTA_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

if(NOT COPYPASTA_SOURCES)
    message(FATAL_ERROR "C++ copypasta has no source files")
endif()

foreach(source IN LISTS COPYPASTA_SOURCES)
    get_filename_component(stem "${source}" NAME_WE)
    add_library("compile_${stem}" OBJECT "${source}")
    target_compile_features("compile_${stem}" PRIVATE cxx_std_17)
endforeach()
