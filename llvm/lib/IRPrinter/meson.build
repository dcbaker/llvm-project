# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_ir_printer = library(
  'LLVMIRPrinter',
  [
    'IRPrintingPasses.cpp',
    gen_intrinsics,
  ],
  include_directories : '../../include/llvm/IRPrinter',
  dependencies : [
    component_analysis, component_core, component_support,
  ],
  install : true,
)

component_ir_printer = declare_dependency(
  link_with : lib_ir_printer,
)
