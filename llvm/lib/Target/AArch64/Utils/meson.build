# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_aarch64_utils = library(
  'LLVMAArch64Utils',
  [
    'AArch64BaseInfo.cpp',
    'AArch64SMEAttributes.cpp',
    gen_aarch64_incs,
  ],
  include_directories : inc_aarch64,
  dependencies : [
    component_support, component_core,
  ],
  install : true,
)

component_target_aarch64_utils = declare_dependency(
  link_with : lib_aarch64_utils,
)
