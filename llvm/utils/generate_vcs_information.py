#!/usr/bin/env python
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

from __future__ import annotations
import argparse
import filecmp
import os
import shutil
import subprocess
import typing

if typing.TYPE_CHECKING:

    class Arguments(typing.Protocol):

        output: str
        name: str
        depfile: str | None


def git_revision() -> str | None:
    p = subprocess.run(
        ['git', 'rev-parse', 'HEAD'],
        stdout=subprocess.PIPE, universal_newlines=True)
    return p.stdout.strip() if p.returncode == 0 else None


def git_repo() -> str | None:
    p = subprocess.run(
        ['git', 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{upstream}'],
        stdout=subprocess.PIPE, universal_newlines=True)
    if p.returncode != 0:
        return None
    remote = p.stdout.split('/', 1)[0]
    p = subprocess.run(
        ['git', 'remote', 'get-url', remote],
        stdout=subprocess.PIPE, universal_newlines=True)
    # TODO: handle passwords and github tokens
    return p.stdout.strip() if p.returncode == 0 else None


def git_head_location() -> str | None:
    p = subprocess.run(
        ['git', 'rev-parse', '--git-dir'],
        stdout=subprocess.PIPE, universal_newlines=True)
    if p.returncode != 0:
        return None
    return os.path.join(p.stdout.strip(), 'logs/HEAD')


def main() -> None:
    # TODO: handle explicit overrides
    parser = argparse.ArgumentParser()
    parser.add_argument('output', help='Where to write the output file.')
    parser.add_argument('name', help='The name of the project.')
    parser.add_argument('--depfile', action='store', help='Optionally, where to write a depfile')
    args = typing.cast('Arguments', parser.parse_args())

    content: list[str] = []
    if rev := git_revision():
        content.append(f'#define {args.name}_REVISION "{rev}"')
    else:
        content.append(f'#undef {args.name}_REVISION')

    if repo := git_repo():
        content.append(f'#define {args.name}_REPOSITORY "{repo}"')
    else:
        content.append(f'#undef {args.name}_REPOSITORY')

    tmp_output = f'{args.output}.tmp'
    with open(tmp_output, 'w', encoding='ascii') as f:
        for c in content:
            f.write(c)
            f.write('\n')

    if not os.path.exists(args.output) or not filecmp.cmp(args.output, tmp_output):
        shutil.move(tmp_output, args.output)
    else:
        os.unlink(tmp_output)

    if args.depfile:
        with open(args.depfile, 'w', encoding='ascii') as f:
            f.write(args.output)
            f.write(': ')
            if x := git_head_location():
                f.write(x)
            f.write('\n')


if __name__ == '__main__':
    main()
