# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_debuginfo_dwarf = library(
  'LLVMDebugInfoDWARF',
  [
    'DWARFAbbreviationDeclaration.cpp',
    'DWARFAddressRange.cpp',
    'DWARFAcceleratorTable.cpp',
    'DWARFCompileUnit.cpp',
    'DWARFContext.cpp',
    'DWARFDataExtractor.cpp',
    'DWARFDebugAbbrev.cpp',
    'DWARFDebugAddr.cpp',
    'DWARFDebugArangeSet.cpp',
    'DWARFDebugAranges.cpp',
    'DWARFDebugFrame.cpp',
    'DWARFDebugInfoEntry.cpp',
    'DWARFDebugLine.cpp',
    'DWARFDebugLoc.cpp',
    'DWARFDebugMacro.cpp',
    'DWARFDebugPubTable.cpp',
    'DWARFDebugRangeList.cpp',
    'DWARFDebugRnglists.cpp',
    'DWARFDie.cpp',
    'DWARFExpression.cpp',
    'DWARFFormValue.cpp',
    'DWARFGdbIndex.cpp',
    'DWARFListTable.cpp',
    'DWARFLocationExpression.cpp',
    'DWARFTypeUnit.cpp',
    'DWARFUnitIndex.cpp',
    'DWARFUnit.cpp',
    'DWARFVerifier.cpp',
  ],
  include_directories : [
    '../../../include/llvm/DebugInfo/DWARF', inc_debuginfo,
  ],
  dependencies : [
    component_binary_format, component_object, component_support,
    component_target_parser,
  ],
  install : true,
)

component_debuginfo_dwarf = declare_dependency(
  link_with : lib_debuginfo_dwarf
)
