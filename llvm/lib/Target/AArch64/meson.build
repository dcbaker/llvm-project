# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

inc_aarch64 = include_directories('.')

# TODO: option interactions
gen_aarch64_incs = []

# TODO: this could be broken up more to allow more parallelism
_gens = [
  ['AArch64GenAsmMatcher.inc', '-gen-asm-matcher'],
  ['AArch64GenAsmWriter.inc', '-gen-asm-writer'],
  ['AArch64GenAsmWriter1.inc', ['-gen-asm-writer', '-asmwriternum=1']],
  ['AArch64GenCallingConv.inc', '-gen-callingconv'],
  ['AArch64GenDAGISel.inc', '-gen-dag-isel'],
  ['AArch64GenDisassemblerTables.inc', '-gen-disassembler'],
  ['AArch64GenFastISel.inc', '-gen-fast-isel'],
  ['AArch64GenGlobalISel.inc', '-gen-global-isel'],
  ['AArch64GenO0PreLegalizeGICombiner.inc', ['-gen-global-isel-combiner', '-combiners=AArch64O0PreLegalizerCombiner']],
  ['AArch64GenPreLegalizeGICombiner.inc', ['-gen-global-isel-combiner', '-combiners=AArch64PreLegalizerCombiner']],
  ['AArch64GenPostLegalizeGICombiner.inc', ['-gen-global-isel-combiner', '-combiners=AArch64PostLegalizerCombiner']],
  ['AArch64GenPostLegalizeGILowering.inc', ['-gen-global-isel-combiner', '-combiners=AArch64PostLegalizerLowering']],
  ['AArch64GenInstrInfo.inc', '-gen-instr-info'],
  ['AArch64GenMCCodeEmitter.inc', '-gen-emitter'],
  ['AArch64GenMCPseudoLowering.inc', '-gen-pseudo-lowering'],
  ['AArch64GenRegisterBank.inc', '-gen-register-bank'],
  ['AArch64GenRegisterInfo.inc', '-gen-register-info'],
  ['AArch64GenSubtargetInfo.inc', '-gen-subtarget'],
  ['AArch64GenSystemOperands.inc', '-gen-searchable-tables'],
  ['AArch64GenExegesis.inc', '-gen-exegesis'],
]

foreach _a : _gens
  output = _a[0]
  args = _a[1]

  gen_aarch64_incs += custom_target(
    command : [
      bin_table_gen, '@INPUT@', '-o', '@OUTPUT@', '-d', '@DEPFILE@',
      '-I' + meson.current_source_dir(),
      '-I' + meson.current_build_dir(),
      '-I' + meson.project_source_root() / 'include',
      '-I' + meson.project_build_root() / 'include',
      '--write-if-changed', args,
    ],
    input : ['AArch64.td'],
    output : [output],
    depfile : f'@output@.d',
  )
endforeach

alias_target('AArch64CommonTableGen', gen_aarch64_incs)

subdir('Utils')
subdir('TargetInfo')
subdir('MCTargetDesc')
subdir('Disassembler')
subdir('AsmParser')

component_target_aarch64 = declare_dependency(
  sources : gen_aarch64_incs,
  dependencies : [
    component_target_aarch64_utils, component_target_aarch64_info,
    component_target_aarch64_desc, component_target_aarch64_disassmebler,
    component_target_aarch64_asm_parser,
  ],
)

lib_aarch64_code_gen = library(
  'LLVMAArch64CodeGen',
  [
    'GISel/AArch64CallLowering.cpp',
    'GISel/AArch64GlobalISelUtils.cpp',
    'GISel/AArch64InstructionSelector.cpp',
    'GISel/AArch64LegalizerInfo.cpp',
    'GISel/AArch64O0PreLegalizerCombiner.cpp',
    'GISel/AArch64PreLegalizerCombiner.cpp',
    'GISel/AArch64PostLegalizerCombiner.cpp',
    'GISel/AArch64PostLegalizerLowering.cpp',
    'GISel/AArch64PostSelectOptimize.cpp',
    'GISel/AArch64RegisterBankInfo.cpp',
    'AArch64A57FPLoadBalancing.cpp',
    'AArch64AdvSIMDScalarPass.cpp',
    'AArch64Arm64ECCallLowering.cpp',
    'AArch64AsmPrinter.cpp',
    'AArch64BranchTargets.cpp',
    'AArch64CallingConvention.cpp',
    'AArch64CleanupLocalDynamicTLSPass.cpp',
    'AArch64CollectLOH.cpp',
    'AArch64CondBrTuning.cpp',
    'AArch64ConditionalCompares.cpp',
    'AArch64DeadRegisterDefinitionsPass.cpp',
    'AArch64ExpandImm.cpp',
    'AArch64ExpandPseudoInsts.cpp',
    'AArch64FalkorHWPFFix.cpp',
    'AArch64FastISel.cpp',
    'AArch64A53Fix835769.cpp',
    'AArch64FrameLowering.cpp',
    'AArch64CompressJumpTables.cpp',
    'AArch64ConditionOptimizer.cpp',
    'AArch64RedundantCopyElimination.cpp',
    'AArch64ISelDAGToDAG.cpp',
    'AArch64ISelLowering.cpp',
    'AArch64InstrInfo.cpp',
    'AArch64LoadStoreOptimizer.cpp',
    'AArch64LowerHomogeneousPrologEpilog.cpp',
    'AArch64MachineFunctionInfo.cpp',
    'AArch64MachineScheduler.cpp',
    'AArch64MacroFusion.cpp',
    'AArch64MIPeepholeOpt.cpp',
    'AArch64MCInstLower.cpp',
    'AArch64PointerAuth.cpp',
    'AArch64PostCoalescerPass.cpp',
    'AArch64PromoteConstant.cpp',
    'AArch64PBQPRegAlloc.cpp',
    'AArch64RegisterInfo.cpp',
    'AArch64SLSHardening.cpp',
    'AArch64SelectionDAGInfo.cpp',
    'AArch64SpeculationHardening.cpp',
    'AArch64StackTagging.cpp',
    'AArch64StackTaggingPreRA.cpp',
    'AArch64StorePairSuppress.cpp',
    'AArch64Subtarget.cpp',
    'AArch64TargetMachine.cpp',
    'AArch64TargetObjectFile.cpp',
    'AArch64TargetTransformInfo.cpp',
    'SMEABIPass.cpp',
    'SMEPeepholeOpt.cpp',
    'SVEIntrinsicOpts.cpp',
    'AArch64SIMDInstrOpt.cpp',
    gen_intrinsics,
  ],
  dependencies : [
    component_target_aarch64,
    component_analysis, component_asm_printer, component_cfguard,
    component_code_gen, component_code_gen_types, component_core,
    component_global_isel, component_mc, component_scalar,
    component_selection_dag, component_support, component_target,
    component_target_parser, component_transform_utils, component_vectorize,
  ],
  install : true,
)

component_target_aarch64 = declare_dependency(
  dependencies : component_target_aarch64,
  link_with : lib_aarch64_code_gen,
)
