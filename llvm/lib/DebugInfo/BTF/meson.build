# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_debuginfo_btf = library(
  'LLVMDebugInfoBTF',
  [
    'BTFParser.cpp',
    'BTFContext.cpp',
  ],
  include_directories : ['../../../include/llvm/DebugInfo/BTF'],
  dependencies : [component_support],
  install : true,
)

component_debuginfo_btf = declare_dependency(
  link_with : lib_debuginfo_btf
)
