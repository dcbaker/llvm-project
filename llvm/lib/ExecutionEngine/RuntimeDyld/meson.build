# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMRuntimeDyld',
  [
    'JITSymbol.cpp',
    'RTDyldMemoryManager.cpp',
    'RuntimeDyld.cpp',
    'RuntimeDyldChecker.cpp',
    'RuntimeDyldCOFF.cpp',
    'RuntimeDyldELF.cpp',
    'RuntimeDyldMachO.cpp',
    'Targets/RuntimeDyldELFMips.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_core, component_mc, component_object, component_support,
    component_target_parser,
  ],
  install : true,
)

component_runtime_dyld = declare_dependency(
  link_with : _lib,
)
