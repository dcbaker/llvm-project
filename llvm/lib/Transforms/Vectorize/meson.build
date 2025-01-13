# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_vectorize = library(
  'LLVMVectorize',
  [
    'LoadStoreVectorizer.cpp',
    'LoopIdiomVectorize.cpp',
    'LoopVectorizationLegality.cpp',
    'LoopVectorize.cpp',
    'SandboxVectorizer/DependencyGraph.cpp',
    'SandboxVectorizer/InstrMaps.cpp',
    'SandboxVectorizer/Interval.cpp',
    'SandboxVectorizer/Legality.cpp',
    'SandboxVectorizer/Passes/BottomUpVec.cpp',
    'SandboxVectorizer/Passes/RegionsFromMetadata.cpp',
    'SandboxVectorizer/SandboxVectorizer.cpp',
    'SandboxVectorizer/SandboxVectorizerPassBuilder.cpp',
    'SandboxVectorizer/Scheduler.cpp',
    'SandboxVectorizer/SeedCollector.cpp',
    'SandboxVectorizer/VecUtils.cpp',
    'SLPVectorizer.cpp',
    'Vectorize.cpp',
    'VectorCombine.cpp',
    'VPlan.cpp',
    'VPlanAnalysis.cpp',
    'VPlanHCFGBuilder.cpp',
    'VPlanRecipes.cpp',
    'VPlanSLP.cpp',
    'VPlanTransforms.cpp',
    'VPlanUnroll.cpp',
    'VPlanVerifier.cpp',
    'VPlanUtils.cpp',
    gen_intrinsics,
  ],
  include_directories : [
    '../../../include/llvm/Transforms',
    '../../../include/llvm/Transforms/Vectorize',
    '../../../include/llvm/Transforms/Vectorize/SandboxVectorizer',
  ],
  dependencies : [
    component_analysis, component_core, component_support,
    component_transform_utils, component_sandbox_ir,
  ],
  install : true,
)

component_vectorize = declare_dependency(
  link_with : lib_vectorize,
)
