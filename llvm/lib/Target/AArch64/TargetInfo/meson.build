# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_aarch64_info = library(
  'LLVMAArch64Info',
  [
    'AArch64TargetInfo.cpp',
    gen_aarch64_incs,
  ],
  include_directories : inc_aarch64,
  dependencies : [
    component_support, component_mc
  ],
  install : true,
)

component_target_aarch64_info = declare_dependency(
  sources : gen_aarch64_incs,
  link_with : lib_aarch64_info,
)
