# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

subdir('Bitstream/Reader')
subdir('Remarks')
subdir('TargetParser')
subdir('BinaryFormat')
subdir('IR')
subdir('FileCheck')
#subdir('Extensions')  # TODO: needs annoying Extension.def
subdir('Bitcode/Reader')
subdir('MC')
subdir('AsmParser')
subdir('IRReader')
subdir('TextAPI')
subdir('Object')
subdir('DebugInfo')
subdir('ProfileData')
subdir('TextAPI/BinaryReader')
subdir('Analysis')
subdir('Bitcode/Writer')
subdir('InterfaceStub')
subdir('IRPrinter')
subdir('CGData')
subdir('SandboxIR')
subdir('Transforms')
subdir('FuzzMutate')
subdir('Frontend')
subdir('Linker')
subdir('Transforms/IPO')
subdir('Transforms/Coroutines')
subdir('Target')
subdir('CodeGen')
foreach t : targets_to_build
  subdir('Target' / t)
endforeach
subdir('DWARFLinker')
#add_subdirectory(LTO)  # TODO: needs Extension
subdir('MCA')
subdir('ObjCopy')
subdir('ObjectYAML')
subdir('Option')
subdir('Debuginfod')
subdir('DWP')
subdir('WindowsDriver')
subdir('Passes')
subdir('ExecutionEngine')
subdir('LineEditor')
if get_option('telemetry')
  subdir('Telemetry')
endif
subdir('ToolDrivers')
#add_subdirectory(XRay)
# TODO: tests
# add_subdirectory(WindowsDriver)
# add_subdirectory(WindowsManifest)

# TODO: component group?
