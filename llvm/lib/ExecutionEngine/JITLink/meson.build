# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_gen = custom_target(
  command : [
    bin_table_gen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
    '--write-if-changed', '-gen-opt-parser-defs',
    '-I' + meson.project_source_root() / 'include',
  ],
  input : ['COFFOptions.td'],
  output : ['COFFOptions.inc'],
  depfile : '@PLAINNAME@.d',
)

alias_target('JITLinkTableGen', _gen)

_lib = library(
  'LLVMJITLink',
  [
    'CompactUnwindSupport.cpp',
    'DWARFRecordSectionSplitter.cpp',
    'EHFrameSupport.cpp',
    'JITLink.cpp',
    'JITLinkGeneric.cpp',
    'JITLinkMemoryManager.cpp',

    # Formats:

    # MachO
    'MachO.cpp',
    'MachO_arm64.cpp',
    'MachO_x86_64.cpp',
    'MachOLinkGraphBuilder.cpp',

    # ELF
    'ELF.cpp',
    'ELFLinkGraphBuilder.cpp',
    'ELF_aarch32.cpp',
    'ELF_aarch64.cpp',
    'ELF_i386.cpp',
    'ELF_loongarch.cpp',
    'ELF_ppc64.cpp',
    'ELF_riscv.cpp',
    'ELF_x86_64.cpp',

    # COFF
    'COFF.cpp',
    'COFFDirectiveParser.cpp',
    'COFFLinkGraphBuilder.cpp',
    'COFF_x86_64.cpp',

    # Architectures:
    'aarch32.cpp',
    'aarch64.cpp',
    'i386.cpp',
    'loongarch.cpp',
    'ppc64.cpp',
    'riscv.cpp',
    'x86_64.cpp',
    gen_intrinsics,
    _gen,
  ],
  include_directories : '../../../include/llvm/ExecutionEngine/JITLink',
  dependencies : [
    # TODO: these are linked privately?
    component_binary_format, component_object, component_option,
    component_orc_target_process, component_support, component_target_parser,
  ],
  install : true,
)

component_jit_link = declare_dependency(
  sources : _gen,
  link_with : _lib,
)
