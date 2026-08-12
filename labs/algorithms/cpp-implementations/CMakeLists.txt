cmake_minimum_required(VERSION 3.23)
project(cpp_implementation_lab LANGUAGES CXX)

file(
    GLOB_RECURSE LAB_SOURCES
    CONFIGURE_DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/algorithms/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/data-structures/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/language/*.cpp"
)

if(NOT LAB_SOURCES)
    message(FATAL_ERROR "C++ implementation lab has no managed source files")
endif()

foreach(source IN LISTS LAB_SOURCES)
    file(RELATIVE_PATH relative_source "${CMAKE_CURRENT_SOURCE_DIR}" "${source}")
    string(MAKE_C_IDENTIFIER "compile_${relative_source}" target_name)
    add_library("${target_name}" OBJECT "${source}")
    target_compile_features("${target_name}" PRIVATE cxx_std_17)
endforeach()
