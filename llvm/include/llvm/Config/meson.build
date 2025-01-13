# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

# This differs from the way CMake does this a lot, and it deserves explanation:
#  1. Meson, by design, does not have globs. That logic would need to be
#     reimplemented in Python, which would be a non-trivial amount of work
#  2. Running globs slows down the configure step and/or makes it less robust.
#     It cannot be robust unless we re-run Meson without exception, since the
#     backend cannot know for certain that something has changed.
#
# Meson does not need to do the "wrong" target check, since the option
# handler already enforces valid values for us

_targets_with_asm_printers = [
  'AArch64', 'AMDGPU', 'ARC', 'ARM', 'AVR', 'BPF', 'CSKY', 'DirectX',
  'Hexagon', 'Lanai', 'LoongArch', 'M68k', 'Mips', 'MSP430', 'NVPTX',
  'PowerPC', 'RISCV', 'Sparc', 'SPIRV', 'SystemZ', 'VE', 'WebAssembly', 'X86',
  'XCore', 'Xtensa',
]

_targets_with_enum_asm_parsers = [
  'AArch64', 'AMDGPU', 'ARM', 'AVR', 'BPF', 'CSKY', 'Hexagon', 'Lanai',
  'LoongArch', 'M68k', 'Mips', 'MSP430', 'PowerPC', 'RISCV', 'Sparc', 'SystemZ',
  'VE', 'WebAssembly', 'X86', 'Xtensa',
]

_targets_with_enum_disassemblers = [
  'AArch64', 'AMDGPU', 'ARC', 'ARM', 'AVR', 'BPF', 'CSKY', 'Hexagon', 'Lanai',
  'LoongArch', 'M68k', 'Mips', 'MSP430', 'PowerPC', 'RISCV', 'Sparc', 'SystemZ',
  'VE', 'WebAssembly', 'X86', 'XCore', 'Xtensa',
]

_targets_with_enum_targetmcas = ['AMDGPU', 'RISCV', 'X86']

_targets_with_enum_exegesis = ['AArch64', 'Mips', 'PowerPC', 'RISCV', 'X86']

_enum_targets = []
_enum_asm_printers = []
_enum_asm_parsers = []
_enum_disassemblers = []
_enum_targetmcas = []
_enum_exegesis = []

foreach t : targets_to_build
  config.set(f'LLVM_HAS_@0@_TARGET'.format(t.to_upper()), 1)
  _enum_targets += f'LLVM_TARGET(@t@)'
  if t in _targets_with_asm_printers
    _enum_asm_printers += f'LLVM_ASM_PRINTER(@t@)'
  endif
  if t in _targets_with_enum_asm_parsers
    _enum_asm_parsers += f'LLVM_ASM_PARSER(@t@)'
  endif
  if t in _targets_with_enum_disassemblers
    _enum_disassemblers += f'LLVM_DISASSEMBLER(@t@)'
  endif
  if t in _targets_with_enum_targetmcas
    _enum_targetmcas += f'LLVM_TARGETMCA(@t@)'
  endif
  if t in _targets_with_enum_exegesis
    _enum_exegesis += f'LLVM_EXEGESIS(@t@)'
  endif
endforeach

config.set('LLVM_ENUM_TARGETS', '\n'.join(_enum_targets) + '\n')
config.set('LLVM_ENUM_ASM_PRINTERS', '\n'.join(_enum_asm_printers) + '\n')
config.set('LLVM_ENUM_ASM_PARSERS', '\n'.join(_enum_asm_parsers) + '\n')
config.set('LLVM_ENUM_DISASSEMBLERS', '\n'.join(_enum_disassemblers) + '\n')
config.set('LLVM_ENUM_TARGETMCAS', '\n'.join(_enum_targetmcas) + '\n')
config.set('LLVM_ENUM_EXEGESIS', '\n'.join(_enum_exegesis) + '\n')

foreach header : ['config.h.cmake', 'llvm-config.h.cmake',
                  'abi-breaking.h.cmake']
  configure_file(
    configuration : config,
    input : header,
    output : '@BASENAME@',
    format : 'cmake',
    # TODO: install?
  )
endforeach

foreach def : ['AsmPrinters', 'AsmParsers', 'Disassemblers', 'Targets',
               'TargetMCAs', 'TargetExegesis']
  configure_file(
    configuration : config,
    input : f'@def@.def.in',
    output : '@BASENAME@',
    format : 'cmake@',
  )
endforeach
