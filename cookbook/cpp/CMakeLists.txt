cmake_minimum_required(VERSION 3.23)
project(cpp_cookbook LANGUAGES CXX)

file(GLOB_RECURSE COOKBOOK_SOURCES CONFIGURE_DEPENDS "*.cpp")

foreach(source IN LISTS COOKBOOK_SOURCES)
    file(RELATIVE_PATH relative_source "${CMAKE_CURRENT_SOURCE_DIR}" "${source}")
    string(MAKE_C_IDENTIFIER "sample_${relative_source}" target_name)
    add_library("${target_name}" OBJECT "${source}")
    target_compile_features("${target_name}" PRIVATE cxx_std_17)
endforeach()
