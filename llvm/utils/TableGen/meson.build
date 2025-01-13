# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

subdir('Common')

bin_table_gen = executable(
  'llvm-tblgen',
  [
    'AsmMatcherEmitter.cpp',
    'AsmWriterEmitter.cpp',
    'CallingConvEmitter.cpp',
    'CodeEmitterGen.cpp',
    'CodeGenMapTable.cpp',
    'CompressInstEmitter.cpp',
    'CTagsEmitter.cpp',
    'DAGISelEmitter.cpp',
    'DAGISelMatcherEmitter.cpp',
    'DAGISelMatcherGen.cpp',
    'DAGISelMatcherOpt.cpp',
    'DecoderEmitter.cpp',
    'DFAEmitter.cpp',
    'DFAPacketizerEmitter.cpp',
    'DisassemblerEmitter.cpp',
    'DXILEmitter.cpp',
    'ExegesisEmitter.cpp',
    'FastISelEmitter.cpp',
    'GlobalISelCombinerEmitter.cpp',
    'GlobalISelEmitter.cpp',
    'InstrDocsEmitter.cpp',
    'InstrInfoEmitter.cpp',
    'llvm-tblgen.cpp',
    'MacroFusionPredicatorEmitter.cpp',
    'OptionParserEmitter.cpp',
    'OptionRSTEmitter.cpp',
    'PseudoLoweringEmitter.cpp',
    'RegisterBankEmitter.cpp',
    'RegisterInfoEmitter.cpp',
    'SDNodeInfoEmitter.cpp',
    'SearchableTableEmitter.cpp',
    'SubtargetEmitter.cpp',
    'WebAssemblyDisassemblerEmitter.cpp',
    'X86InstrMappingEmitter.cpp',
    'X86DisassemblerTables.cpp',
    'X86FoldTablesEmitter.cpp',
    'X86MnemonicTables.cpp',
    'X86ModRMFilters.cpp',
    'X86RecognizableInstr.cpp',
    gen_intrinsics,
  ],
  link_whole : lib_table_gen_basic,
  dependencies : [
    component_code_gen_types, component_support, dep_table_gen_common,
  ],
  # TODO: install
)

alias_target('llvm-tblgen', bin_table_gen)
