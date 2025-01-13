# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

gen_acc = []

foreach _s : [['h.inc', 'decl'], ['inc', 'impl']]
  out = _s[0]
  cmd = _s[1]
  gen_acc += custom_target(
    command : [
      prog_min_tblgen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
      '-I' + meson.current_source_dir(), '-I' + meson.current_build_dir(),
      '-I' + meson.project_source_root() / 'include', '-I' + meson.project_build_root() / 'include',
      '--write-if-changed', f'--gen-directive-@cmd@',
    ],
    input : ['ACC.td'],
    output : [f'ACC.@out@'],
    depfile : f'ACC.@out@.d',
  )
endforeach

alias_target('acc_gen', gen_acc)
