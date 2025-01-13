# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_table_gen_basic = static_library(
  'LLVMTableGenBasic',
  'ARMTargetDefEmitter.cpp',
  'Attributes.cpp',
  'CodeGenIntrinsics.cpp',
  'DirectiveEmitter.cpp',
  'IntrinsicEmitter.cpp',
  'RISCVTargetDefEmitter.cpp',
  'SDNodeProperties.cpp',
  'TableGen.cpp',
  'VTEmitter.cpp',
  dependencies : [component_support, component_table_gen],
)

prog_min_tblgen = executable(
  'llvm-min-tblgen',
  '../llvm-min-tblgen.cpp',
  dependencies : [component_support],
  link_whole : lib_table_gen_basic,
)

alias_target('llvm-min-tblgen', prog_min_tblgen)
