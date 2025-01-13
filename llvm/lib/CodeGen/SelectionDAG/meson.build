# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_selection_dag = library(
  'LLVMSelectionDAG',
  [
    'DAGCombiner.cpp',
    'FastISel.cpp',
    'FunctionLoweringInfo.cpp',
    'InstrEmitter.cpp',
    'LegalizeDAG.cpp',
    'LegalizeFloatTypes.cpp',
    'LegalizeIntegerTypes.cpp',
    'LegalizeTypes.cpp',
    'LegalizeTypesGeneric.cpp',
    'LegalizeVectorOps.cpp',
    'LegalizeVectorTypes.cpp',
    'ResourcePriorityQueue.cpp',
    'ScheduleDAGFast.cpp',
    'ScheduleDAGRRList.cpp',
    'ScheduleDAGSDNodes.cpp',
    'ScheduleDAGVLIW.cpp',
    'SelectionDAGBuilder.cpp',
    'SelectionDAG.cpp',
    'SelectionDAGAddressAnalysis.cpp',
    'SelectionDAGDumper.cpp',
    'SelectionDAGISel.cpp',
    'SelectionDAGPrinter.cpp',
    'SelectionDAGTargetInfo.cpp',
    'StatepointLowering.cpp',
    'TargetLowering.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_analysis, component_code_gen, component_code_gen_types,
    component_core, component_mc, component_support, component_target,
    component_target_parser, component_transform_utils,
  ],
  install : true,
)

component_selection_dag = declare_dependency(
  link_with : lib_selection_dag,
)
