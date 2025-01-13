# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_inc_root = '../../../include/llvm/Frontend'

lib_frontend_openmp = library(
  'LLVMFrontendOpenMP',
  [
    'OMP.cpp',
    'OMPContext.cpp',
    'OMPIRBuilder.cpp',
    gen_omp,
    gen_intrinsics,
  ],
  include_directories : [_inc_root, _inc_root / 'OpenMP'],
  dependencies : [
    component_core, component_support, component_target_parser,
    component_transform_utils, component_analysis, component_demangle,
    component_mc, component_scalar, component_bit_reader,
    component_frontend_atomic, component_frontend_offloading,
  ],
  install : true,
)

component_frontend_openmp = declare_dependency(
  link_with : lib_frontend_openmp,
)


