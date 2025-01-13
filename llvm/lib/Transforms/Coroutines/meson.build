# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMCoroutines',
  [
    'Coroutines.cpp',
    'CoroAnnotationElide.cpp',
    'CoroCleanup.cpp',
    'CoroConditionalWrapper.cpp',
    'CoroEarly.cpp',
    'CoroElide.cpp',
    'CoroFrame.cpp',
    'CoroSplit.cpp',
    'SuspendCrossingInfo.cpp',
    'SpillUtils.cpp',
    'MaterializationUtils.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/Transforms/Coroutines',
  dependencies : [
    component_analysis, component_core, component_ipo, component_scalar,
    component_support, component_transform_utils, component_target_parser,
  ],
  install : true,
)

component_coroutines = declare_dependency(
  link_with : _lib,
)
