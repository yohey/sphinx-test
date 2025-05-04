cmake_minimum_required(VERSION 3.12)

project(mypackage Fortran)

add_library(mypackage SHARED)

target_sources(mypackage
  PRIVATE
  src/ffi/ffi_test.f90
)

target_compile_options(mypackage
  PRIVATE
  -std=f2018
)

set_target_properties(mypackage PROPERTIES
  PUBLIC_HEADER
  src/ffi/ffi_test.h
)

install(TARGETS mypackage
  LIBRARY DESTINATION       lib
  PUBLIC_HEADER DESTINATION include/mypackage
)


add_subdirectory(src/python)
