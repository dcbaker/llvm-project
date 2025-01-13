# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_object_yaml = library(
  'LLVMObjectYAML',
  [
    'ArchiveEmitter.cpp',
    'ArchiveYAML.cpp',
    'CodeViewYAMLDebugSections.cpp',
    'CodeViewYAMLSymbols.cpp',
    'CodeViewYAMLTypeHashing.cpp',
    'CodeViewYAMLTypes.cpp',
    'COFFEmitter.cpp',
    'COFFYAML.cpp',
    'DWARFEmitter.cpp',
    'DWARFYAML.cpp',
    'DXContainerEmitter.cpp',
    'DXContainerYAML.cpp',
    'ELFEmitter.cpp',
    'ELFYAML.cpp',
    'GOFFEmitter.cpp',
    'GOFFYAML.cpp',
    'MachOEmitter.cpp',
    'MachOYAML.cpp',
    'ObjectYAML.cpp',
    'MinidumpEmitter.cpp',
    'MinidumpYAML.cpp',
    'OffloadEmitter.cpp',
    'OffloadYAML.cpp',
    'WasmEmitter.cpp',
    'WasmYAML.cpp',
    'XCOFFEmitter.cpp',
    'XCOFFYAML.cpp',
    'YAML.cpp',
    'yaml2obj.cpp',
  ],
  include_directories : '../../include/llvm/ObjectYAML',
  dependencies : [
    component_binary_format, component_object, component_support,
    component_target_parser, component_debuginfo_code_view, component_mc,
  ],
  install : true,
)

component_object_yaml = declare_dependency(
  link_with : lib_object_yaml,
)
