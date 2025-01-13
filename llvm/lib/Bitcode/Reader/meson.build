# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_bit_reader = library(
  'LLVMBitReader',
  [
    'BitcodeAnalyzer.cpp',
    'BitReader.cpp',
    'BitcodeReader.cpp',
    'MetadataLoader.cpp',
    'ValueList.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/Bitcode',
  dependencies : [
    component_bitstream_reader, component_core, component_support,
    component_target_parser,
  ],
  install : true,
)

component_bit_reader = declare_dependency(
  link_with : lib_bit_reader,
)
