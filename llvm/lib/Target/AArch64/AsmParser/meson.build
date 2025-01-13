# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_aarch64_asm_parser = library(
  'LLVMAArch64AsmParser',
  [
    'AArch64AsmParser.cpp',
    gen_aarch64_incs,
  ],
  include_directories : inc_aarch64,
  dependencies : [
    component_target_aarch64_info, component_target_aarch64_utils,
    component_target_aarch64_desc, component_code_gen_types, component_mc,
    component_mc_parser, component_support, component_target_parser,
  ],
  install : true,
)

component_target_aarch64_asm_parser = declare_dependency(
  sources : gen_aarch64_incs,
  link_with : lib_aarch64_asm_parser,
)
