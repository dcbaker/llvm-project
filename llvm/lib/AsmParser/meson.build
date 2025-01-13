# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_asm_parser = library(
  'LLVMAsmParser',
  [
    'LLLexer.cpp',
    'LLParser.cpp',
    'Parser.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_binary_format, component_core, component_support,
  ],  install : true,
)

component_asm_parser = declare_dependency(
  link_with : lib_asm_parser,
)
