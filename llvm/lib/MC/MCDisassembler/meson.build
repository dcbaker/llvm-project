# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_mc_disassembler = library(
  'LLVMMCDisassembler',
  [
    'Disassembler.cpp',
    'MCDisassembler.cpp',
    'MCExternalSymbolizer.cpp',
    'MCRelocationInfo.cpp',
    'MCSymbolizer.cpp',
  ],
  dependencies : [
    component_mc, component_support, component_target_parser,
  ],
  install : true,
)

component_mc_disassembler = declare_dependency(
  link_with : lib_mc_disassembler,
)
