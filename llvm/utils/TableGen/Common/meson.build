# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_table_gen_common = static_library(
  'LLVMTableGenCommon',
  [
    'GlobalISel/CodeExpander.cpp',
    'GlobalISel/CombinerUtils.cpp',
    'GlobalISel/CXXPredicates.cpp',
    'GlobalISel/GlobalISelMatchTable.cpp',
    'GlobalISel/GlobalISelMatchTableExecutorEmitter.cpp',
    'GlobalISel/PatternParser.cpp',
    'GlobalISel/Patterns.cpp',

    'AsmWriterInst.cpp',
    'CodeGenDAGPatterns.cpp',
    'CodeGenHwModes.cpp',
    'CodeGenInstAlias.cpp',
    'CodeGenInstruction.cpp',
    'CodeGenRegisters.cpp',
    'CodeGenSchedule.cpp',
    'CodeGenTarget.cpp',
    'DAGISelMatcher.cpp',
    'InfoByHwMode.cpp',
    'OptEmitter.cpp',
    'PredicateExpander.cpp',
    'SubtargetFeatureInfo.cpp',
    'Types.cpp',
    'Utils.cpp',
    'VarLenCodeEmitterGen.cpp',
    gen_vt,
    gen_intrinsics,
  ],
  include_directories : [include_directories('..')],
  link_whole : lib_table_gen_basic,
  dependencies : [component_support, component_table_gen],
  install : true,
)

dep_table_gen_common = declare_dependency(
  sources : [gen_vt, gen_intrinsics],
  link_with : lib_table_gen_common,
  include_directories : [include_directories('..')],
)
