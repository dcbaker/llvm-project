# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_aggressive_inst_combine = library(
  'LLVMAggressiveInstCombine',
  [
    'AggressiveInstCombine.cpp',
    'TruncInstCombine.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms',
    '../../../include/llvm/Transforms/AggressiveInstCombine',
  ],
  dependencies : [
    component_analysis, component_core, component_support,
    component_transform_utils,
  ],
  install : true,
)

component_aggressive_inst_combine = declare_dependency(
  link_with : lib_aggressive_inst_combine,
)

