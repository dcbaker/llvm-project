# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMPasses',
  [
    'CodeGenPassBuilder.cpp',
    'DroppedVariableStatsIR.cpp',
    'OptimizationLevel.cpp',
    'PassBuilder.cpp',
    'PassBuilderBindings.cpp',
    'PassBuilderPipelines.cpp',
    'PassPlugin.cpp',
    'StandardInstrumentations.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/Passes',
  dependencies : [
    component_aggressive_inst_combine, component_analysis, component_cfguard,
    component_code_gen, component_core, component_coroutines,
    component_hipstdpar, component_ipo, component_inst_combine,
    component_ir_printer, component_objcarc, component_scalar,
    component_support, component_target, component_transform_utils,
    component_vectorize, component_instrumentation,
  ],
  install : true,
)

component_passes = declare_dependency(
  link_with : _lib,
)
