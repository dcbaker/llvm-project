# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_debuginfo_msf = library(
  'LLVMDebugInfoMSF',
  [
    'MappedBlockStream.cpp',
    'MSFBuilder.cpp',
    'MSFCommon.cpp',
    'MSFError.cpp',
  ],
  include_directories : '../../../include/llvm/DebugInfo/MSF',
  dependencies : component_support,
  install : true,
)

component_debuginfo_msf = declare_dependency(
  link_with : lib_debuginfo_msf,
)
