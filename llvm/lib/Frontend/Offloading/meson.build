# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_frontend_offloading = library(
  'LLVMFrontendOffloading',
  [
    'Utility.cpp',
    'OffloadWrapper.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/Frontend',
  dependencies : [
    component_core, component_binary_format, component_object,
    component_support, component_transform_utils, component_target_parser,
  ],
  install : true,
)

component_frontend_offloading = declare_dependency(
  link_with : lib_frontend_offloading,
)


