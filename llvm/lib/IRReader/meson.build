# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_ir_reader = library(
  'LLVMIRReader',
  [
    'IRReader.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/IRReader',
  dependencies : [
    component_asm_parser, component_bit_reader, component_core,
    component_support,
  ],
  install : true,
)

component_ir_reader = declare_dependency(
  link_with : lib_ir_reader,
)
