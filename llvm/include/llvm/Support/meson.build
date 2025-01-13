# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

gen_vcs_revision_h = custom_target(
  command : [
    meson.project_source_root() / 'utils/generate_vcs_information.py',
    '@OUTPUT@', 'LLVM', '--depfile', '@DEPFILE@'
  ],
  output : ['VCSRevision.h'],
  depfile : 'VCSRevision.h.d',
)

alias_target('llvm_vcsrevision_h', gen_vcs_revision_h)
