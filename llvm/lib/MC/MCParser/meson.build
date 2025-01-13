# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_mc_parser = library(
  'LLVMMCParser',
  [
    'AsmLexer.cpp',
    'AsmParser.cpp',
    'COFFAsmParser.cpp',
    'COFFMasmParser.cpp',
    'GOFFAsmParser.cpp',
    'DarwinAsmParser.cpp',
    'ELFAsmParser.cpp',
    'MCAsmLexer.cpp',
    'MCAsmParser.cpp',
    'MCAsmParserExtension.cpp',
    'MCTargetAsmParser.cpp',
    'MasmParser.cpp',
    'WasmAsmParser.cpp',
    'XCOFFAsmParser.cpp',
  ],
  include_directories : '../../../include/llvm/MC/MCParser',
  dependencies : [
    component_mc, component_support, component_target_parser,
  ],
  install : true,
)

component_mc_parser = declare_dependency(
  link_with : lib_mc_parser,
)
