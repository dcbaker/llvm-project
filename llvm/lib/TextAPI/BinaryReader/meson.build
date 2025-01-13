# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_text_api_binary_reader = library(
  'LLVMTextAPIBinaryReader',
  'DylibReader.cpp',
  dependencies : [
    component_debuginfo_dwarf, component_support, component_object,
    component_text_api, component_target_parser,
  ],
  install : true,
)

component_text_api_binary_reader = declare_dependency(
  link_with : lib_text_api_binary_reader,
)
