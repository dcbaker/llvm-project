# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_interface_stub = library(
  'LLVMInterfaceStub',
  [
    'ELFObjHandler.cpp',
    'IFSHandler.cpp',
    'IFSStub.cpp',
  ],
  dependencies : [
    component_binary_format, component_mc, component_object, component_support,
    component_target_parser,
  ],
  install : true,
)

component_interface_stub = declare_dependency(
  link_with : lib_interface_stub,
)
