# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation


lib_debuginfo_code_view = library(
  'LLVMDebugInfoCodeView',
  [
    'AppendingTypeTableBuilder.cpp',
    'CodeViewError.cpp',
    'CodeViewRecordIO.cpp',
    'ContinuationRecordBuilder.cpp',
    'CVSymbolVisitor.cpp',
    'CVTypeVisitor.cpp',
    'DebugChecksumsSubsection.cpp',
    'DebugCrossExSubsection.cpp',
    'DebugCrossImpSubsection.cpp',
    'DebugFrameDataSubsection.cpp',
    'DebugInlineeLinesSubsection.cpp',
    'DebugLinesSubsection.cpp',
    'DebugStringTableSubsection.cpp',
    'DebugSubsection.cpp',
    'DebugSubsectionRecord.cpp',
    'DebugSubsectionVisitor.cpp',
    'DebugSymbolRVASubsection.cpp',
    'DebugSymbolsSubsection.cpp',
    'EnumTables.cpp',
    'Formatters.cpp',
    'GlobalTypeTableBuilder.cpp',
    'LazyRandomTypeCollection.cpp',
    'Line.cpp',
    'MergingTypeTableBuilder.cpp',
    'RecordName.cpp',
    'RecordSerialization.cpp',
    'SimpleTypeSerializer.cpp',
    'StringsAndChecksums.cpp',
    'SymbolDumper.cpp',
    'SymbolRecordHelpers.cpp',
    'SymbolRecordMapping.cpp',
    'SymbolSerializer.cpp',
    'TypeDumpVisitor.cpp',
    'TypeIndex.cpp',
    'TypeIndexDiscovery.cpp',
    'TypeHashing.cpp',
    'TypeRecordHelpers.cpp',
    'TypeRecordMapping.cpp',
    'TypeStreamMerger.cpp',
    'TypeTableCollection.cpp',
  ],
  include_directories : '../../../include/llvm/DebugInfo/CodeView',
  dependencies : component_support,
  install : true,
)

component_debuginfo_code_view = declare_dependency(
  link_with : lib_debuginfo_code_view
)
