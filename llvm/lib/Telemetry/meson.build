# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMTelemetry',
  [
    'Telemetry.cpp',
  ],
  include_directories : '../../include/llvm/Telemetry',
  dependencies : [component_support],
  install : true,
)

component_telemetry = declare_dependency(
  link_with : _lib,
)
