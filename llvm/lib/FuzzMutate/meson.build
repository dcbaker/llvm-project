# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_inc = include_directories('../../include/llvm/FuzzMutate')

lib_fuzzer_cli = library(
  'LLVMFuzzerCLI',
  'FuzzerCLI.cpp',
  include_directories : _inc,
  dependencies : [component_support, component_target_parser],
  install : true,
)

component_fuzzer_cli = declare_dependency(
  link_with : lib_fuzzer_cli,
)

lib_fuzzer_mutate = library(
  'LLVMFuzzMutate',
  [
    'IRMutator.cpp',
    'OpDescriptor.cpp',
    'Operations.cpp',
    'RandomIRBuilder.cpp',
    gen_intrinsics,
  ],
  include_directories : _inc,
  dependencies : [
    component_analysis, component_bit_reader, component_bit_writer,
    component_core, component_scalar, component_support,
    component_target_parser, component_transform_utils,
  ],
  install : true,
)

compnoent_fuzz_mutate = declare_dependency(
  link_with : lib_fuzzer_mutate,
)
