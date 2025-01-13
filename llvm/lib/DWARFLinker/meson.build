# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_dwarf_linker = library(
  'LLVMDWARFLinker',
  [
    'DWARFLinkerBase.cpp',
    'Utils.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/DWARFLinker',
  dependencies : [
    component_binary_format, component_code_gen, component_debuginfo_dwarf,
    component_object, component_support,
  ],
  install : true,
)

component_dwarf_linker = declare_dependency(
  link_with : lib_dwarf_linker,
)

subdir('Classic')
subdir('Parallel')
