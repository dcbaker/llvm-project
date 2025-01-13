# SPDX-License-Identifier: <<spdxid>>
# Copyright © 2025 Intel Corporation

_blake3_sources = []
_blake3_c_args = []

# The BLAKE3 team recommends using the assembly versions, from the README:
#
# "For each of the x86 SIMD instruction sets, four versions are available:
# three flavors of assembly (Unix, Windows MSVC, and Windows GNU) and one
# version using C intrinsics. The assembly versions are generally
# preferred. They perform better, they perform more consistently across
# different compilers, and they build more quickly."
if host_machine.cpu_family() == 'x86_64'
  if cpp.get_id() == 'msvc'
    # TODO: MASM
  elif host_machine.system() in ['windows', 'cygwin']
    # TODO: Windows GAS files
  endif
    # TODO: clang 7 workaround
    _blake3_sources = [
      'blake3_sse2_x86-64_unix.S', 'blake3_sse41_x86-64_unix.S',
      'blake3_avx2_x86-64_unix.S', 'blake3_avx512_x86-64_unix.S',
    ]
else
  _blake3_c_args += [
    '-DBLAKE3_NO_AVX512', '-DBLAKE3_NO_AVX2', '-DBLAKE_NO_SSE41',
    '-DBLAKE3_NO_SSE2',
  ]
endif

# FIXME: This is an object library in CMake, but Meson doesn't have those
lib_blake3 = static_library(
  'LLVMSupportBlake3',
  'blake3.c',
  'blake3_dispatch.c',
  'blake3_portable.c',
  'blake3_neon.c',
  _blake3_sources,
  c_args : _blake3_c_args,
)

dep_blake3 = declare_dependency(
  link_whole : lib_blake3,
)
