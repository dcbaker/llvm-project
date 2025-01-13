# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation


lib_symbolize = library(
  'LLVMSymbolize',
  [
    'DIPrinter.cpp',
    'Markup.cpp',
    'MarkupFilter.cpp',
    'SymbolizableObjectFile.cpp',
    'Symbolize.cpp',
  ],
  include_directories : ['../../../include/llvm/DebugInfo/Symbolize'],
  dependencies : [
    component_debuginfo_dwarf, component_debuginfo_pdb, component_debuginfo_btf,
    component_object, component_support, component_demangle,
    component_target_parser,
  ],
  install : true,
)

component_symbolize = declare_dependency(
  link_with : lib_symbolize,
)
