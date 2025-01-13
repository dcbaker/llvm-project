# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_frontend_atomic = library(
  'LLVMFrontendAtomic',
  'Atomic.cpp',
  include_directories : '../../../include/llvm/Frontend/Atomic',
  dependencies : [
    component_core, component_support, component_analysis,
  ],
  install : true,
)

component_frontend_atomic = declare_dependency(
  link_with : lib_frontend_atomic,
)
