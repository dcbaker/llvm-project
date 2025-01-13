# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_debuginfo_gsym = library(
  'LLVMDebugInfoGSYM',
  [
    'DwarfTransformer.cpp',
    'Header.cpp',
    'FileWriter.cpp',
    'FunctionInfo.cpp',
    'GsymCreator.cpp',
    'GsymReader.cpp',
    'InlineInfo.cpp',
    'LineTable.cpp',
    'LookupResult.cpp',
    'CallSiteInfo.cpp',
    'MergedFunctionsInfo.cpp',
    'ObjectFileTransformer.cpp',
    'ExtractRanges.cpp',
  ],
  include_directories : ['../../../include/llvm/DebugInfo/GSYM', inc_debuginfo],
  dependencies : [
    dep_threads,
    component_mc, component_object, component_support, component_target_parser,
    component_debuginfo_dwarf,
  ],
  install : true,
)

component_debuginfo_gsym = declare_dependency(
  link_with : lib_debuginfo_gsym,
)
