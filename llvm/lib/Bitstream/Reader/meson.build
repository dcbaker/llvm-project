# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_bitstream_reader = library(
  'LLVMBitstreamReader',
  'BitstreamReader.cpp',
  include_directories : [
    '../../../include/llvm/Bitcode',
    '../../../include/llvm/Bitstream',
  ],
  dependencies : [component_support],
  install : true,
)

component_bitstream_reader = declare_dependency(
  link_with : lib_bitstream_reader,
)
