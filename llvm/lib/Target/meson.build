# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_target = library(
  'LLVMTarget',
  [
    'Target.cpp',
    'TargetIntrinsicInfo.cpp',
    'TargetLoweringObjectFile.cpp',
    'TargetMachine.cpp',
    'TargetMachineC.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/Target',
  dependencies : [
    component_analysis,
    component_core,
    component_mc,
    component_support,
    component_target_parser,
  ],
  install : true,
)

component_target = declare_dependency(
  link_with : lib_target,
)
