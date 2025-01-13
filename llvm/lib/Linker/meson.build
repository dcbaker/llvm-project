# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_linker = library(
  'LLVMLinker',
  [
    'IRMover.cpp',
    'LinkModules.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/Linker/',
  dependencies : [
    component_core, component_object, component_support,
    component_transform_utils, component_target_parser,
  ],
  install : true,
)

component_linker = declare_dependency(
  link_with : lib_linker,
)
