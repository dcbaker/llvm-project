# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

_lib = library(
  'LLVMDebuginfod',
  [
    'BuildIDFetcher.cpp',
    'Debuginfod.cpp',
    'HTTPClient.cpp',
    'HTTPServer.cpp',
  ],
  include_directories : '../../include/llvm/Debuginfod',
  dependencies : [
    dep_curl, dep_httplib, dep_threads,
    component_support, component_symbolize, component_debuginfo_dwarf,
    component_binary_format, component_object,
  ],
  install : true,
)

# This is not a component, since it could pull libcurl into libLLVM
dep_debuginfod = declare_dependency(
  link_with : _lib,
)
