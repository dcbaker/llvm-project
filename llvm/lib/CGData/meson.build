# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_cg_data = library(
  'LLVMCGData',
  [
    'CodeGenData.cpp',
    'CodeGenDataReader.cpp',
    'CodeGenDataWriter.cpp',
    'OutlinedHashTree.cpp',
    'OutlinedHashTreeRecord.cpp',
    'StableFunctionMap.cpp',
    'StableFunctionMapRecord.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_bit_reader, component_bit_writer, component_core,
    component_support, component_object,
  ],
  install : true,
)

component_cg_data = declare_dependency(
  link_with : lib_cg_data,
)
