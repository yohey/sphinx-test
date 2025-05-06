
set(SPHINX_APIDOC_EXECUTABLE "sphinx-apidoc" CACHE STRING "Path to sphinx-apidoc executable")
set(SPHINX_BUILD_EXECUTABLE  "sphinx-build"  CACHE STRING "Path to sphinx-build executable")

set(SPHINX_ORIG_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(SPHINX_COPY_SOURCE_DIR ${CMAKE_BINARY_DIR}/docs/source)
set(SPHINX_HTML_OUTPUT_DIR ${CMAKE_BINARY_DIR}/docs/html)
set(SPHINX_APIDOC_OUTPUT_DIR ${SPHINX_COPY_SOURCE_DIR}/generated)
set(PYTHON_PACKAGE_DIR ${CMAKE_SOURCE_DIR}/src/python/mypackage)

add_custom_command(
  OUTPUT ${SPHINX_COPY_SOURCE_DIR}/index.rst
  COMMAND ${CMAKE_COMMAND} -E copy_directory ${SPHINX_ORIG_SOURCE_DIR} ${SPHINX_COPY_SOURCE_DIR}
  COMMENT "Copying Sphinx documentation source to build directory"
  VERBATIM
)

add_custom_target(copy_sphinx_sources
  DEPENDS ${SPHINX_COPY_SOURCE_DIR}/index.rst
)

add_custom_command(
  OUTPUT  ${SPHINX_APIDOC_OUTPUT_DIR}/mypackage.rst
  COMMAND ${SPHINX_APIDOC_EXECUTABLE}
          -o ${SPHINX_APIDOC_OUTPUT_DIR}
          ${PYTHON_PACKAGE_DIR}
          --force
          --no-toc
          --separate
  DEPENDS copy_sphinx_sources
  COMMENT "Generating API documentation using sphinx-apidoc"
  VERBATIM
)

add_custom_target(apidoc
  DEPENDS ${SPHINX_APIDOC_OUTPUT_DIR}/mypackage.rst
)

set(SPHINX_ENV_DEFINITION "PYTHONPATH=${CMAKE_SOURCE_DIR}/src/python")

if(APPLE)
  set(SPHINX_ENV_DEFINITION "${SPHINX_ENV_DEFINITION};DYLD_LIBRARY_PATH=${CMAKE_BINARY_DIR}")
elseif(UNIX)
  set(SPHINX_ENV_DEFINITION "${SPHINX_ENV_DEFINITION};LD_LIBRARY_PATH=${CMAKE_BINARY_DIR}")
elseif(WIN32)
  set(SPHINX_ENV_DEFINITION "${SPHINX_ENV_DEFINITION};PATH=${CMAKE_BINARY_DIR}\;$ENV{PATH}")
endif()

add_custom_target(doc
  COMMAND ${CMAKE_COMMAND} -E env
          ${SPHINX_ENV_DEFINITION}
          ${SPHINX_BUILD_EXECUTABLE} -q
            -b html
            ${SPHINX_COPY_SOURCE_DIR}
            ${SPHINX_HTML_OUTPUT_DIR}
  DEPENDS apidoc mypackage
  COMMENT "Building HTML documentation with sphinx-build"
  VERBATIM
)

set_directory_properties(PROPERTIES
    ADDITIONAL_MAKE_CLEAN_FILES "${SPHINX_HTML_OUTPUT_DIR}"
)
