# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMWindowsDriver',
  [
    'MSVCPaths.cpp',
  ],
  include_directories : '../../include/llvm/WindowsDriver',
  dependencies : [
    component_option, component_support, component_target_parser,
  ],
  install : true,
)

component_windows_driver = declare_dependency(
  link_with : _lib,
)
