# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMMCJIT',
  [
    'MCJIT.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_core, component_execution_engine, component_object,
    component_runtime_dyld, component_support, component_target,
  ],
  install : true,
)

component_mc_jit = declare_dependency(
  link_with : _lib,
)
