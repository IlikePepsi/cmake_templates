cmake_minimum_required(VERSION 3.6)
project(external_toolchain)

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

set(TO_PROCESS ${CMAKE_CURRENT_LIST_DIR}/auxiliary.h)
set(PROCESSED_PATTERN -proc)
set(PROCESSED_FILES "greeter${PROCESSED_PATTERN}.h")

set(HELPER_SCRIPT external_toolchain.sh)
set(HELPER_SCRIPT_OPTIONS "${HELPER_SCRIPT_OPTIONS} --prefix ${CMAKE_CURRENT_LIST_DIR}")

if (CMAKE_BUILD_TYPE STREQUAL Debug)
	set(HELPER_SCRIPT_OPTIONS "${HELPER_SCRIPT_OPTIONS} --debug")
endif ()

set(TOOLCHAIN ${CMAKE_CURRENT_LIST_DIR}/totally_awesome_compiler.py)

configure_file(${HELPER_SCRIPT}.in ${CMAKE_CURRENT_LIST_DIR}/scripts/${HELPER_SCRIPT} @ONLY)

add_custom_command(OUTPUT ${PROCESSED_FILES}
    COMMAND ${CMAKE_CURRENT_LIST_DIR}/scripts/${HELPER_SCRIPT} ${HELPER_SCRIPT_OPTIONS} compile
    COMMENT "Process auxiliary code"
    VERBATIM)

add_custom_target(delete_processed_files)

add_custom_command(TARGET delete_processed_files
    COMMAND ${CMAKE_CURRENT_LIST_DIR}/scripts/${HELPER_SCRIPT} ${HELPER_SCRIPT_OPTIONS} remove
    COMMENT "Delete processed files"
    VERBATIM)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_COMPILER g++)

include_directories(
    ${CMAKE_CURRENT_LIST_DIR}
    ${CMAKE_CURRENT_BINARY_DIR})

add_executable(${PROJECT_NAME} main.cpp ${PROCESSED_FILES})
add_dependencies(${PROJECT_NAME} delete_processed_files)
