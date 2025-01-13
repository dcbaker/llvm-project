# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

gen_target_definitions = []

foreach a : ['ARM', 'AArch64', 'RISCV']
  _root = meson.project_source_root() / 'lib/Target' / a

  _t = custom_target(
    command : [
      prog_min_tblgen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
      '-I' + meson.project_source_root() / 'include', '-I' + meson.project_build_root() / 'include',
      '-I' + _root, '--write-if-changed',
      '-gen-@0@-target-def'.format(a == 'RISCV' ? 'riscv' : 'arm'),
    ],
    input : [_root / f'@a@.td'],
    output : [f'@a@TargetParserDef.inc'],
    depfile : f'@a@TargetParserDef.inc.d',
  )

  alias_target(f'@a@TargetParserTableGen', _t)
  gen_target_definitions += _t
endforeach

