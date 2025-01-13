# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_inst_combine = library(
  'LLVMInstCombine',
  [
    'InstructionCombining.cpp',
    'InstCombineAddSub.cpp',
    'InstCombineAtomicRMW.cpp',
    'InstCombineAndOrXor.cpp',
    'InstCombineCalls.cpp',
    'InstCombineCasts.cpp',
    'InstCombineCompares.cpp',
    'InstCombineLoadStoreAlloca.cpp',
    'InstCombineMulDivRem.cpp',
    'InstCombineNegator.cpp',
    'InstCombinePHI.cpp',
    'InstCombineSelect.cpp',
    'InstCombineShifts.cpp',
    'InstCombineSimplifyDemanded.cpp',
    'InstCombineVectorOps.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms',
    '../../../include/llvm/Transforms/InstCombine',
  ],
  dependencies : [
    component_analysis, component_core, component_support,
    component_transform_utils,
  ],
  install : true,
)

component_inst_combine = declare_dependency(
  link_with : lib_inst_combine,
)

