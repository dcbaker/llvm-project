# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_aarch64_disassmebler = library(
  'LLVMAArch64Disassembler',
  [
    'AArch64Disassembler.cpp',
    'AArch64ExternalSymbolizer.cpp',
    gen_aarch64_incs,
  ],
  include_directories : inc_aarch64,
  dependencies : [
    component_target_aarch64_info, component_target_aarch64_utils,
    component_target_aarch64_desc, component_mc, component_mc_disassembler,
    component_support,
  ],
  install : true,
)

component_target_aarch64_disassmebler = declare_dependency(
  sources : gen_aarch64_incs,
  link_with : lib_aarch64_disassmebler,
)
