# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_global_isel = library(
  'LLVMGlobalISel',
  [
    'CSEInfo.cpp',
    'GISelKnownBits.cpp',
    'CSEMIRBuilder.cpp',
    'CallLowering.cpp',
    'GlobalISel.cpp',
    'Combiner.cpp',
    'CombinerHelper.cpp',
    'CombinerHelperArtifacts.cpp',
    'CombinerHelperCasts.cpp',
    'CombinerHelperCompares.cpp',
    'CombinerHelperVectorOps.cpp',
    'GIMatchTableExecutor.cpp',
    'GISelChangeObserver.cpp',
    'IRTranslator.cpp',
    'InlineAsmLowering.cpp',
    'InstructionSelect.cpp',
    'InstructionSelector.cpp',
    'LegalityPredicates.cpp',
    'LegalizeMutations.cpp',
    'Legalizer.cpp',
    'LegalizerHelper.cpp',
    'LegalizerInfo.cpp',
    'LegacyLegalizerInfo.cpp',
    'LoadStoreOpt.cpp',
    'Localizer.cpp',
    'LostDebugLocObserver.cpp',
    'MachineIRBuilder.cpp',
    'RegBankSelect.cpp',
    'Utils.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../../include/llvm/CodeGen/GlobalISel',
  dependencies : [
    component_analysis, component_code_gen, component_code_gen_types,
    component_core, component_mc, component_selection_dag, component_support,
    component_target, component_transform_utils,
  ],
  install : true,
)

component_global_isel = declare_dependency(
  link_with : lib_global_isel,
)
