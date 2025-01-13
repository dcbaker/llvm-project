# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_remarks = library(
  'LLVMRemarks',
  [
    'BitstreamRemarkParser.cpp',
    'BitstreamRemarkSerializer.cpp',
    'Remark.cpp',
    'RemarkFormat.cpp',
    'RemarkLinker.cpp',
    'RemarkParser.cpp',
    'RemarkSerializer.cpp',
    'RemarkStreamer.cpp',
    'RemarkStringTable.cpp',
    'YAMLRemarkParser.cpp',
    'YAMLRemarkSerializer.cpp',
    gen_intrinsics,
  ],
  include_directories : ['../../../include/llvm/Remarks'],
  dependencies : [component_bitstream_reader, component_support],
  install : true,
)

component_remarks = declare_dependency(
  sources : gen_intrinsics,
  link_with : lib_remarks,
)
