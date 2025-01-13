# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMInstrumentation',
  [
    'AddressSanitizer.cpp',
    'BoundsChecking.cpp',
    'CGProfile.cpp',
    'ControlHeightReduction.cpp',
    'DataFlowSanitizer.cpp',
    'GCOVProfiling.cpp',
    'BlockCoverageInference.cpp',
    'MemProfiler.cpp',
    'MemorySanitizer.cpp',
    'NumericalStabilitySanitizer.cpp',
    'IndirectCallPromotion.cpp',
    'InstrOrderFile.cpp',
    'InstrProfiling.cpp',
    'KCFI.cpp',
    'LowerAllowCheckPass.cpp',
    'PGOCtxProfFlattening.cpp',
    'PGOCtxProfLowering.cpp',
    'PGOForceFunctionAttrs.cpp',
    'PGOInstrumentation.cpp',
    'PGOMemOPSizeOpt.cpp',
    'SanitizerCoverage.cpp',
    'SanitizerBinaryMetadata.cpp',
    'ValueProfileCollector.cpp',
    'ThreadSanitizer.cpp',
    'TypeSanitizer.cpp',
    'HWAddressSanitizer.cpp',
    'RealtimeSanitizer.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms',
  ],
  dependencies : [
    component_analysis, component_core, component_demangle,
    component_mc, component_support, component_target_parser,
    component_transform_utils, component_profile_data,
  ],
  install : true,
)

component_instrumentation = declare_dependency(
  link_with : _lib,
)

