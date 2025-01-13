# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_table_gen = static_library(
  'LLVMTableGen',
  'DetailedRecordsBackend.cpp',
  'Error.cpp',
  'JSONBackend.cpp',
  'Main.cpp',
  'Parser.cpp',
  'Record.cpp',
  'SetTheory.cpp',
  'StringMatcher.cpp',
  'TableGenBackend.cpp',
  'TableGenBackendSkeleton.cpp',
  'TGLexer.cpp',
  'TGParser.cpp',
  'TGTimer.cpp',
  dependencies : [component_support],
)

component_table_gen = declare_dependency(
  link_with : lib_table_gen,
  dependencies : component_support,
)
