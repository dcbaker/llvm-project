# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_frontend_driver = library(
  'LLVMFrontendDriver',
  'CodeGenOptions.cpp',
  include_directories : '../../../include/llvm/Frontend/Driver',
  dependencies : [
    component_core, component_support, component_analysis,
  ],
  install : true,
)

component_frontend_driver = declare_dependency(
  link_with : lib_frontend_driver,
)

