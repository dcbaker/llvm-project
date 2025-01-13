# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_inc_root = '../../../include/llvm/Frontend'

lib_frontend_openacc = library(
  'LLVMFrontendOpenACC',
  [
    'ACC.cpp',
    gen_acc
  ],
  include_directories : [_inc_root, _inc_root / 'OpenACC'],
  dependencies : [component_support],
  install : true,
)

component_frontend_openacc = declare_dependency(
  link_with : lib_frontend_openacc,
)


