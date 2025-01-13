# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_inc = '../../include/llvm/ObjCopy'

lib_obj_copy = library(
  'LLVMObjCopy',
  [
    'Archive.cpp',
    'CommonConfig.cpp',
    'ObjCopy.cpp',
    'ConfigManager.cpp',
    'COFF/COFFObjcopy.cpp',
    'COFF/COFFObject.cpp',
    'COFF/COFFReader.cpp',
    'COFF/COFFWriter.cpp',
    'ELF/ELFObjcopy.cpp',
    'ELF/ELFObject.cpp',
    'MachO/MachOObjcopy.cpp',
    'MachO/MachOReader.cpp',
    'MachO/MachOWriter.cpp',
    'MachO/MachOLayoutBuilder.cpp',
    'MachO/MachOObject.cpp',
    'wasm/WasmObject.cpp',
    'wasm/WasmReader.cpp',
    'wasm/WasmWriter.cpp',
    'wasm/WasmObjcopy.cpp',
    'XCOFF/XCOFFObjcopy.cpp',
    'XCOFF/XCOFFReader.cpp',
    'XCOFF/XCOFFWriter.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    _inc, _inc / 'COFF', _inc / 'ELF', _inc / 'MachO', _inc / 'wasm',
    _inc / 'XCOFF', 'COFF', 'ELF', 'MachO', 'wasm', 'XCOFF',
  ],
  dependencies : [
    component_binary_format, component_object, component_support, component_mc,
  ],
  install : true,
)

component_obj_copy = declare_dependency(
  link_with : lib_obj_copy,
)
