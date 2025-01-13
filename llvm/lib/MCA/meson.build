# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_mca = library(
  'LLVMMCA',
  [
    'CodeEmitter.cpp',
    'Context.cpp',
    'CustomBehaviour.cpp',
    'HWEventListener.cpp',
    'HardwareUnits/HardwareUnit.cpp',
    'HardwareUnits/LSUnit.cpp',
    'HardwareUnits/RegisterFile.cpp',
    'HardwareUnits/ResourceManager.cpp',
    'HardwareUnits/RetireControlUnit.cpp',
    'HardwareUnits/Scheduler.cpp',
    'IncrementalSourceMgr.cpp',
    'InstrBuilder.cpp',
    'Instruction.cpp',
    'Pipeline.cpp',
    'Stages/DispatchStage.cpp',
    'Stages/EntryStage.cpp',
    'Stages/ExecuteStage.cpp',
    'Stages/InOrderIssueStage.cpp',
    'Stages/InstructionTables.cpp',
    'Stages/MicroOpQueueStage.cpp',
    'Stages/RetireStage.cpp',
    'Stages/Stage.cpp',
    'Support.cpp',
    'View.cpp',
  ],
  include_directories : '../../include/llvm/MCA',
  dependencies : [component_mc, component_support],
  install : true,
)

component_mca = declare_dependency(
  link_with : lib_mca,
)
