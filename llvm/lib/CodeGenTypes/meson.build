# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_codegentypes = library(
  'LLVMCodeGenTypoes',
  [
    'LowLevelType.cpp',
    gen_vt,
  ],
  dependencies : component_support,
  install : true,
)

component_code_gen_types = declare_dependency(
  link_with : lib_codegentypes,
)
