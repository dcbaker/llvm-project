# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMDWP',
  [
    'DWP.cpp',
    'DWPError.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/DWP',
  dependencies : [
    component_debuginfo_dwarf, component_mc, component_object,
    component_support,
  ],
  install : true,
)

component_dwp = declare_dependency(
  link_with : _lib,
)
