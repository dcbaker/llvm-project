# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_inc_root = '../../../include/llvm/Frontend'

lib_frontend_hlsl = library(
  'LLVMFrontendHLSL',
  'HLSLResource.cpp',
  include_directories : [_inc_root, _inc_root / 'HLSL'],
  dependencies : [
    component_core, component_support,
  ],
  install : true,
)

component_frontend_hlsl = declare_dependency(
  link_with : lib_frontend_hlsl,
)

