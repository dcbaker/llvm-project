# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMOption',
  [
    'Arg.cpp',
    'ArgList.cpp',
    'Option.cpp',
    'OptTable.cpp',
  ],
  include_directories : '../../include/llvm/Option',
  dependencies : [component_support],
  install : true,
)

component_option = declare_dependency(
  link_with : _lib,
)
