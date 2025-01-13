# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_dwarf_linker_parallel = library(
  'LLVMDWARFLinkerParallel',
  [
    'AcceleratorRecordsSaver.cpp',
    'DependencyTracker.cpp',
    'DIEAttributeCloner.cpp',
    'DWARFEmitterImpl.cpp',
    'DWARFLinker.cpp',
    'DWARFLinkerCompileUnit.cpp',
    'DWARFLinkerTypeUnit.cpp',
    'DWARFLinkerImpl.cpp',
    'DWARFLinkerUnit.cpp',
    'OutputSections.cpp',
    'SyntheticTypeNameBuilder.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_asm_printer, component_binary_format, component_code_gen,
    component_debuginfo_dwarf, component_dwarf_linker, component_mc,
    component_object, component_support, component_target_parser,
    dep_threads,
  ],
  install : true,
)

component_dwarf_linker_classic = declare_dependency(
  link_with : lib_dwarf_linker_classic,
)

