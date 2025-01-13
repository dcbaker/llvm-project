# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMOrcShared',
  [
    'AllocationActions.cpp',
    'MachOObjectFormat.cpp',
    'ObjectFormats.cpp',
    'OrcError.cpp',
    'OrcRTBridge.cpp',
    'SimpleRemoteEPCUtils.cpp',
    'SymbolStringPool.cpp',
    gen_intrinsics,
  ],
  include_directories : inc_orc,
  dependencies : [dep_threads, component_support],
  install : true,
)

component_orc_shared = declare_dependency(
  link_with : _lib,
)
