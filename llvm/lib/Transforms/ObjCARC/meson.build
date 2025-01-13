# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_objc_arc_opts = library(
  'LLVMObjCARCOpts',
  [
    'ObjCARC.cpp',
    'ObjCARCOpts.cpp',
    'ObjCARCExpand.cpp',
    'ObjCARCAPElim.cpp',
    'ObjCARCContract.cpp',
    'DependencyAnalysis.cpp',
    'ProvenanceAnalysis.cpp',
    'ProvenanceAnalysisEvaluator.cpp',
    'PtrState.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms',
  ],
  dependencies : [
    component_analysis, component_core, component_support,
    component_transform_utils,
  ],
  install : true,
)

component_objcarc = declare_dependency(
  link_with : lib_objc_arc_opts,
)
