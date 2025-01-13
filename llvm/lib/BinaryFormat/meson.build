# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_binary_format = library(
  'LLVMBinaryFormat',
  [
    'AMDGPUMetadataVerifier.cpp',
    'COFF.cpp',
    'Dwarf.cpp',
    'DXContainer.cpp',
    'ELF.cpp',
    'MachO.cpp',
    'Magic.cpp',
    'Minidump.cpp',
    'MsgPackDocument.cpp',
    'MsgPackDocumentYAML.cpp',
    'MsgPackReader.cpp',
    'MsgPackWriter.cpp',
    'Wasm.cpp',
    'XCOFF.cpp',
  ],
  include_directories : ['../../../include/llvm/BinaryFormat'],
  dependencies : [component_support, component_target_parser],
  install : true,
)

component_binary_format = declare_dependency(
  link_with : lib_binary_format,
)
