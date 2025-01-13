# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_bit_writer = library(
  'LLVMBitWriter',
  [
    'BitWriter.cpp',
    'BitcodeWriter.cpp',
    'BitcodeWriterPass.cpp',
    'ValueEnumerator.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_analysis, component_core, component_mc, component_object,
    component_profile_data, component_support, component_target_parser,
  ],
  install : true,
)

component_bit_writer = declare_dependency(
  link_with : lib_bit_writer,
)
