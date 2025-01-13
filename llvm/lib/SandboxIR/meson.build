# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_sandbox_ir = library(
  'LLVMSandboxIR',
  [
    'Argument.cpp',
    'BasicBlock.cpp',
    'Constant.cpp',
    'Context.cpp',
    'Function.cpp',
    'Instruction.cpp',
    'Module.cpp',
    'Pass.cpp',
    'PassManager.cpp',
    'Region.cpp',
    'Tracker.cpp',
    'Type.cpp',
    'User.cpp',
    'Use.cpp',
    'Value.cpp',
  ],
  dependencies : [
    component_core, component_support, component_analysis,
  ],
  install : true,
)

component_sandbox_ir = declare_dependency(
  link_with : lib_sandbox_ir,
)


