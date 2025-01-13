# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

# TODO: intel_target_profiling

_lib = library(
  'LLVMOrcTargetProcess',
  [
    'ExecutorSharedMemoryMapperService.cpp',
    'DefaultHostBootstrapValues.cpp',
    'JITLoaderGDB.cpp',
    'JITLoaderPerf.cpp',
    'JITLoaderVTune.cpp',
    'OrcRTBootstrap.cpp',
    'RegisterEHFrames.cpp',
    'SimpleExecutorDylibManager.cpp',
    'SimpleExecutorMemoryManager.cpp',
    'SimpleRemoteEPCServer.cpp',
    'TargetExecutionUtils.cpp',
    'UnwindInfoManager.cpp',
  ],
  include_directories : inc_orc,
  dependencies : [
    dep_threads, dep_rt, component_support, component_target_parser,
    component_orc_shared,
  ],
  install : true,
)

component_orc_target_process = declare_dependency(
  link_with : _lib,
)
