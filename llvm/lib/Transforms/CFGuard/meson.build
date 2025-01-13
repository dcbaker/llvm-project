# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_cfguard = library(
  'LLVMCFGuard',
  [
    'CFGuard.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms',
  ],
  dependencies : [
    component_core, component_support, component_target_parser,
  ],
  install : true,
)

component_cfguard = declare_dependency(
  link_with : lib_cfguard,
)
