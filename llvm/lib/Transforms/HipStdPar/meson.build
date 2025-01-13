# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_hip_std_par = library(
  'LLVMHipStdPar',
  [
    'HipStdPar.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms/HipStdPar',
  ],
  dependencies : [
    component_analysis, component_core, component_support,
    component_transform_utils,
  ],
  install : true,
)

component_hipstdpar = declare_dependency(
  link_with : lib_hip_std_par,
)
