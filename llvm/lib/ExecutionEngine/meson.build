# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

inc_orc = include_directories('../../../include/llvm/ExecutionEngine/Orc')

subdir('RuntimeDyld')
subdir('Orc/Shared')
subdir('Orc/TargetProcess')

_lib = library(
  'LLVMExecutionEngine',
  [
    'ExecutionEngine.cpp',
    'ExecutionEngineBindings.cpp',
    'GDBRegistrationListener.cpp',
    'SectionMemoryManager.cpp',
    'TargetSelect.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/ExecutionEngine',
  dependencies : [
    component_core, component_mc, component_object,
    component_orc_target_process, component_runtime_dyld, component_support,
    component_target, component_target_parser,
  ],
  install : true,
)

component_execution_engine = declare_dependency(
  link_with : _lib,
)

# TODO: INTEL_JIT_EVENTS
# TODO: subdir(IntelJITProfiling)
# TODO: subdir(IntelJITEvents)

subdir('Interpreter')
subdir('JITLink')
subdir('MCJIT')
subdir('Orc')

# TODO: LLVM_USE_OPROFILE
# TODO: LLVM_USE_PERF
