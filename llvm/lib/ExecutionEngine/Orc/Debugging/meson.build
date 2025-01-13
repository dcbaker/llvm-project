# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMOrcDebugging',
  [
    'DebugInfoSupport.cpp',
    'DebuggerSupport.cpp',
    'DebuggerSupportPlugin.cpp',
    'LLJITUtilsCBindings.cpp',
    'PerfSupportPlugin.cpp',
    'VTuneSupportPlugin.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../../include/llvm/ExecutionEngine/Orc/Debugging/',
  dependencies : [
    dep_threads, dep_rt, # TODO: atomic
    component_binary_format, component_debuginfo_dwarf, component_jit_link,
    component_orc_jit, component_orc_shared, component_support,
    component_target_parser,
  ],
  install : true,
)

component_orc_debugging = declare_dependency(
  link_with : _lib,
)
