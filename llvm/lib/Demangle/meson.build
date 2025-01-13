# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

lib_llvmdemangle = static_library(
  'LLVMDemangle',
  [
    'Demangle.cpp',
    'ItaniumDemangle.cpp',
    'MicrosoftDemangle.cpp',
    'MicrosoftDemangleNodes.cpp',
    'RustDemangle.cpp',
    'DLangDemangle.cpp',
  ],
  install : true,
)

component_demangle = declare_dependency(
  link_with : lib_llvmdemangle,
)
