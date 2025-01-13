# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_aarch64_desc = library(
  'LLVMAArch64Desc',
  [
    'AArch64AsmBackend.cpp',
    'AArch64ELFObjectWriter.cpp',
    'AArch64ELFStreamer.cpp',
    'AArch64InstPrinter.cpp',
    'AArch64MCAsmInfo.cpp',
    'AArch64MCCodeEmitter.cpp',
    'AArch64MCExpr.cpp',
    'AArch64MCTargetDesc.cpp',
    'AArch64MachObjectWriter.cpp',
    'AArch64TargetStreamer.cpp',
    'AArch64WinCOFFObjectWriter.cpp',
    'AArch64WinCOFFStreamer.cpp',
    gen_aarch64_incs,
  ],
  include_directories : inc_aarch64,
  dependencies : [
    component_target_aarch64_info, component_target_aarch64_utils,
    component_binary_format, component_code_gen_types,
    component_mc, component_support, component_target_parser,
  ],
  install : true,
)

component_target_aarch64_desc = declare_dependency(
  sources : gen_aarch64_incs,
  link_with : lib_aarch64_desc,
)
