# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMInterpreter',
  [
    'Execution.cpp',
    'ExternalFunctions.cpp',
    'Interpreter.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    dep_ffi,
    component_code_gen, component_core, component_execution_engine,
    component_support,
  ],
  install : true,
)

component_interpreter = declare_dependency(
  link_with : _lib,
)
