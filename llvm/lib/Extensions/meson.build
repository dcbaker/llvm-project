# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

# TODO: need Extension.def to be generated

lib_extensions = library(
  'LLVMExtensions',
  'Extensions.cpp',
  dependencies : component_support,
  install : true,
)

component_extensions = declare_dependency(
  link_with : lib_extensions,
)
