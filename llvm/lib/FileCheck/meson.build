# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_file_check = library(
  'LLVMFileCheck',
  'FileCheck.cpp',
  include_directories : '../../include/llvm/FileCheck',
  dependencies : component_support,
  install : true,
)

component_file_check = declare_dependency(
  link_with : lib_file_check,
)
