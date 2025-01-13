# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

# TODO: use -Werror=global-constructors

lib_target_parser = library(
  'LLVMTargetParser',
  [
    'AArch64TargetParser.cpp',
    'ARMTargetParserCommon.cpp',
    'ARMTargetParser.cpp',
    'CSKYTargetParser.cpp',
    'Host.cpp',
    'LoongArchTargetParser.cpp',
    'PPCTargetParser.cpp',
    'RISCVISAInfo.cpp',
    'RISCVTargetParser.cpp',
    'SubtargetFeature.cpp',
    'TargetParser.cpp',
    'Triple.cpp',
    'X86TargetParser.cpp',
    gen_target_definitions,
  ],
  include_directories : [include_directories('Unix', 'Windows')],
  dependencies : [component_support],
  install : true,
)

component_target_parser = declare_dependency(
  sources : [gen_target_definitions],
  link_with : lib_target_parser,
  # TODO: Solaris kstat
)
