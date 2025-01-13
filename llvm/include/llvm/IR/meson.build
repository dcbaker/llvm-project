# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

# TODO: table-gen extra arguments
# TODO: lsp server yaml stuff
gen_intrinsics = []

_includes = ['-I' + meson.current_source_dir(), '-I' + meson.current_build_dir()]

gen_intrinsics += custom_target(
  command : [
    prog_min_tblgen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
    '--write-if-changed', _includes, '-gen-attrs',
  ],
  input : ['Attributes.td'],
  output : ['Attributes.inc'],
  depfile : 'Attributes.inc.d',
)

_includes += [
  '-I' + meson.project_source_root() / 'include',
  '-I' + meson.project_build_root() / 'include',
]

gen_intrinsics += custom_target(
  command : [
    prog_min_tblgen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
    '--write-if-changed', _includes, '-gen-intrinsic-impl',
  ],
  input : ['Intrinsics.td'],
  output : ['IntrinsicImpl.inc'],
  depfile : 'IntrinsicsImpl.inc.d',
)

gen_intrinsics += custom_target(
  command : [
    prog_min_tblgen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
    '--write-if-changed', _includes,
    '-gen-intrinsic-enums',
  ],
  input : ['Intrinsics.td'],
  output : ['IntrinsicEnums.inc'],
  depfile : 'IntrinsicEnums.inc.d',
)

foreach _v : [['AArch64', 'aarch64'], ['AMDGPU', 'amdgcn'], ['ARM', 'arm'],
              ['BPF', 'bpf'], ['DirectX', 'dx'], ['Hexagon', 'hexagon'],
              ['LoongArch', 'loongarch'], ['Mips', 'mips'], ['NVPTX', 'nvvm'],
              ['PowerPC', 'ppc'], ['R600', 'r600'], ['RISCV', 'riscv'],
              ['SPIRV', 'spv'], ['S390', 's390'], ['WebAssembly', 'wasm'],
              ['X86', 'x86'], ['XCore', 'xcore'], ['VE', 've']]
  arch = _v[0]
  prefix=_v[1]
  gen_intrinsics += custom_target(
    command : [
      prog_min_tblgen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
      '--write-if-changed', _includes,
      '-gen-intrinsic-enums', f'-intrinsic-prefix=@prefix@',
    ],
    input : ['Intrinsics.td'],
    output : [f'Intrinsics@arch@.h'],
    depfile : f'Intrinsics@arch@.h.d',
  )
endforeach

alias_target('intrinsics_gen', gen_intrinsics)
