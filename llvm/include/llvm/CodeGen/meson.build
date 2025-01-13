# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

# TODO: table-gen extra arguments
# TODO: lsp server yaml stuff
gen_vt = custom_target(
  command : [
    prog_min_tblgen, '--write-if-changed', '-gen-vt',
    '-I' + meson.current_source_dir(), '-I' + meson.current_build_dir(),
    '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
  ],
  input : ['ValueTypes.td'],
  output : ['GenVT.inc'],
  depfile : 'GenVt.inc.d',
)

alias_target('vt_gen', gen_vt)
