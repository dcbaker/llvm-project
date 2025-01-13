# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_ir_parser = library(
  'LLVMIRParser',
  [
    'MILexer.cpp',
    'MIParser.cpp',
    'MIRParser.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/CodeGen/MIRParser',
  dependencies : [
    component_asm_parser, component_binary_format, component_code_gen,
    component_code_gen_types, component_core, component_mc, component_support,
    component_target,
  ],
  install : true,
)

component_ir_parser = declare_dependency(
  link_with : lib_ir_parser,
)
