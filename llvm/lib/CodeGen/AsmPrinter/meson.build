# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_asm_printer = library(
  'LLVMAsmPrinter',
  [
    'AccelTable.cpp',
    'AddressPool.cpp',
    'AIXException.cpp',
    'ARMException.cpp',
    'AsmPrinter.cpp',
    'AsmPrinterDwarf.cpp',
    'AsmPrinterInlineAsm.cpp',
    'DbgEntityHistoryCalculator.cpp',
    'DebugHandlerBase.cpp',
    'DebugLocStream.cpp',
    'DIE.cpp',
    'DIEHash.cpp',
    'DwarfCFIException.cpp',
    'DwarfCompileUnit.cpp',
    'DwarfDebug.cpp',
    'DwarfExpression.cpp',
    'DwarfFile.cpp',
    'DwarfStringPool.cpp',
    'DwarfUnit.cpp',
    'EHStreamer.cpp',
    'ErlangGCPrinter.cpp',
    'OcamlGCPrinter.cpp',
    'PseudoProbePrinter.cpp',
    'WinCFGuard.cpp',
    'WinException.cpp',
    'CodeViewDebug.cpp',
    'WasmException.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_analysis, component_binary_format, component_code_gen,
    component_code_gen_types, component_core, component_debuginfo_code_view,
    component_debuginfo_dwarf, component_mc, component_mc_parser,
    component_remarks, component_support, component_target,
    component_target_parser,
  ],
  install : true,
)

component_asm_printer = declare_dependency(
  link_with : lib_asm_printer,
)
