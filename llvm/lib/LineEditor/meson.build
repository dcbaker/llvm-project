# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMLineEditor',
  [
    'LineEditor.cpp',
  ],
  include_directories : '../../include/llvm/LineEditor',
  dependencies : [dep_libedit, component_support],
  install : true,
)

component_line_editor = declare_dependency(
  link_with : _lib,
)
