# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_text_api = library(
  'LLVMTextAPI',
  [
    'Architecture.cpp',
    'ArchitectureSet.cpp',
    'InterfaceFile.cpp',
    'TextStubV5.cpp',
    'PackedVersion.cpp',
    'Platform.cpp',
    'RecordsSlice.cpp',
    'RecordVisitor.cpp',
    'Symbol.cpp',
    'SymbolSet.cpp',
    'Target.cpp',
    'TextAPIError.cpp',
    'TextStub.cpp',
    'TextStubCommon.cpp',
    'Utils.cpp',
  ],
  include_directories : '../../include/llvm/TextAPI',
  dependencies : [
    component_support, component_binary_format, component_target_parser,
  ],
  install : true,
)

component_text_api = declare_dependency(
  link_with : lib_text_api,
)
