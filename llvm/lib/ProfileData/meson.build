# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_profile_data = library(
  'LLVMProfileData',
  [
    'GCOV.cpp',
    'InstrProf.cpp',
    'InstrProfCorrelator.cpp',
    'InstrProfReader.cpp',
    'InstrProfWriter.cpp',
    'ItaniumManglingCanonicalizer.cpp',
    'MemProf.cpp',
    'MemProfReader.cpp',
    'PGOCtxProfReader.cpp',
    'PGOCtxProfWriter.cpp',
    'ProfileSummaryBuilder.cpp',
    'SampleProf.cpp',
    'SampleProfReader.cpp',
    'SampleProfWriter.cpp',
    'SymbolRemappingReader.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/ProfileData',
  dependencies : [
    component_bitstream_reader, component_core, component_object,
    component_support, component_demangle, component_symbolize,
    component_debuginfo_dwarf, component_target_parser,
  ],
  install : true,
)

component_profile_data = declare_dependency(
  link_with : lib_profile_data,
)
