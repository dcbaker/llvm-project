# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_gen = custom_target(
  command : [
    bin_table_gen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
    '--write-if-changed', '-gen-opt-parser-defs',
    '-I' + meson.project_source_root() / 'include',
  ],
  input : ['Options.td'],
  output : ['@BASENAME@.inc'],
  depfile : '@PLAINNAME@.d',
)

alias_target('LibOptionsTableGen', _gen)

_lib = library(
  'LLVMLibDriver',
  [
    'LibDriver.cpp',
    _gen,
  ],
  dependencies : [
    component_binary_format, component_bit_reader, component_object,
    component_option, component_support,
  ],
  install : true,
)

component_telemetry = declare_dependency(
  link_with : _lib,
)
