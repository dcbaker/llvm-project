# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Copyright © 2025 Intel Corporation

project(
  'LLVM',
  'c', 'cpp',
  version : '20.1.8',
  meson_version : '>= 1.3.0',  # somewhat arbitrary
  license : 'Apache-2.0 WITH LLVM-exception',
  license_files : 'LICENSE.TXT',
  default_options : [
    'cpp_std=c++17', 'b_ndebug=if-release', 'default_library=static',
  ],
)

# TODO: overrides
config = configuration_data()
config.set('PACKAGE_NAME', meson.project_name())
config.set('PACKAGE_STRING',
           '@0@ @1@'.format(meson.project_name(), meson.project_version()))
config.set('PACKAGE_VERSION', meson.project_version())
package_version = meson.project_version().split('.')
config.set('LLVM_VERSION_MAJOR', package_version[0])
config.set('LLVM_VERSION_MINOR', package_version[1])
config.set('LLVM_VERSION_PATCH', package_version[2])

cpp = meson.get_compiler('cpp')
cc = meson.get_compiler('c')

# Widely used system provided dependencies
deps_system = []

fs = import('fs')

# TODO: override shlib version?
# TODO: libdir suffix
# TODO: cygwin extensions
# TODO: side-by-side mode
# TODO: llvm_all_projects - should this be meson.metaproject?
# TODO: llvm_extra_projects - should this be meson.metaproject?

# TODO: libc gpu?
# TODO: llvm_runtime_targets
# TODO: llvm_enable_projects

# TODO: need more ccache stuff. Likely need some Meson patches since Meson
#       handles  ccache/sccache internally

# TODO: LLVM_DEPENDENCY_DEBUGGING
# TODO: LLVM_ENABLE_DAGISEL_COV
# TODO: LLVM_ENABLE_GISEL_COV
# TODO: LLVM_INSTALL_*_SYMLINKS
# TODO: LLVM_USE_SYMLINKS
# TODO: LLVM_INSTALL_UTILS
# TODO: LLVM_INSTALL_TOOLCHAIN_ONLY
# TODO: LLVM_INSTALL_MODULE_MAPS
# TODO: LLVM_USE_FOLDERS?
# TODO: LLVM_APPEND_VS_REV | LLVM_FORCE_VC_REVISION
# TODO: LLVM_TOOL_LLVM_DRIVER_BUILD

# TODO: options for this
config.set('BUG_REPORT_URL', 'https://github.com/llvm/llvm-project/issues/')

# TODO: more bug report uls
# TODO: install dir overrides

all_targets = [
  'AArch64',
  'AMDGPU',
  'ARM',
  'AVR',
  'BPF',
  'Hexagon',
  'Lanai',
  'LoongArch',
  'Mips',
  'MSP430',
  'NVPTX',
  'PowerPC',
  'RSICV',
  'Sparc',
  'SPIRV',
  'SystemZ',
  'VE',
  'WebAssembly',
  'X86',
  'XCore',
]

# TODO: experimental_targets

targets_with_jit = [
  'X86',
  'PowerPC',
  'AArch64',
  'ARM',
  'MIPS',
  'SystemZ',
]

if get_option('backtraces')
  config.set('ENABLE_BACKTRACES', 1)
endif

if get_option('crash-overrides')
  config.set('ENABLE_CRASH_OVERRIDES', 1)
endif

# TODO: LLVM_ENABLE_UNWIND_TABLES
# TODO: LLVM_ENABLE_CRASH_DUMPS
# TODO: LLVM_ENABLE_DEBUGLOC_COVERAGE_TRACKING
# TODO: WINDOWS_PREFER_FORWARD_SLASH_DEFAULT ?
# TODO: threads
# TODO: Z3

targets_to_build = get_option('targets') + get_option('experimental-targets')
summary('Targeting', targets_to_build)

# FIXME: Do we need to ensure that b_staticpic == b_pie?
config.set10('ENABLE_PIC', get_option('b_staticpic'))

# TODO: OS390 pic
# TODO: C++ modules
# TODO: ENABLE_LOCAL_SUBMODULE
# TODO: ENABLE_LIBCXX
# TODO: ENABLE_LLVM_LIBC
# TODO: ENABLE_LINK_CXX_STDLIB
# TODO: ENABLE_LLD
# TODO: ENABLE_DUMP
# TODO: ENABLE_UNREACHABLE_OPTIMIZE
# TODO: ENABLE_EXPENSIVE_CHECKS
# TODO: ENABLE_STRICT_FIXED_SIZE_VECTORS
# TODO: ENABLE_ABI_BREAKING_CHECKS
# TODO: ENABLE_FORCE_USE_OLD_TOOLCHAIN
# TODO: ENABLE_TEMPORARILY_ALLOW_OLD_TOOLCHAIN
# TODO: ENABLE_LOCAL_RPATH - I think this is unnecessary
# TODO: USE_INTEL_JIT_EVENTS
# TODO: USE_OPROFILE
# TODO: EXTERNALIZE_DEBUGINFO
# TODO: EXPORTED_SYMBOLS_IN_EXECUTABLES
# TODO: CODESIGNING_IDENTITY
# TODO: USE_PERF
# TODO: UBSAN_FLAGS - maybe nothing, maybe handle because of default?
# TODO: SPLIT_DWARF
# TODO: lit options
# TODO: ENABLE_RPMALLOC
# TODO: INTEGRATED_CRT_ALLOC
# TODO: LLVM_DYLIB_COMPONENTS
# TODO: LLVM_C_DYLIB
# TODO: llvm_build_llvm_dylib_vis
# TODO: LLVM_BUILD_LLVM_DYLIB
# TODO: LLVM_BUILD_LLVM_DYLIB_INLINES
# TODO: LLVM_LINK_LLVM_DYLIB
# TODO: LLVM_OPTIMIZED_TABLEGEN
# TODO: LLVM_OMIT_DAGISEL_COMMENTS
# TODO: LLVM_ADD_NATIVE_VISUALIZERS_TO_SOLUTION
# TODO: profile and test coverage - may be covered by Meson builtins
# TODO: LLVM_TARGET_TRIPLE_ENV
# TODO: LLVM_ENABLE_PER_TARGET_RUNTIME_DIR
# TODO: LLVM_PROFDATA_FILE
# TODO: Minimum Python version

# The contents of config-ix equivalent

# TODO: include(CheckIncludeFile)
# TODO: include(CheckLibraryExists)
# TODO: include(CheckSymbolExists)
# TODO: include(CheckCXXSymbolExists)
# TODO: include(CheckFunctionExists)
# TODO: include(CheckStructHasMemberExists)
# TODO: include(CheckCCompilerFlag)
# TODO: include(CheckCSourceCompiles)
# TODO: include(CMakePushCheckState)
# TODO: include(CheckCompilerVersionCheckState)
# TODO: include(HandleLLVMStdlib)

# This allows the library to be found, but provides an "empty" library if there
# is no libm, and is universally portable
deps_system += cpp.find_library('m', required : false)

# TODO: FreeBSD 9.2 libcxxrt workaround
# TODO: AIX

if cc.has_header_symbol('stdlib.h', '__GLIBC__')
  add_project_arguments('-D_GNU_SOURCE', language : ['c', 'cpp'])
endif

_headers = [
  'dlfcn.h', 'errno.h', 'fcntl.h', 'malloc/malloc.h', 'signal.h', 'sys/ioctl.h',
  'sys/mman.h', 'sys/resource.h', 'sys/stat.h', 'sys/time.h', 'sysexits.h',
  'termios.h', 'unistd.h', 'fenv.h', 'mach/mach.h', 'CrashReporterClient.h'
]
# Meson differentiates MinGW, Cygwin, and "Pure" Windows
if host_machine.system() != 'windows'
  _headers += 'pthread.h'
endif
if host_machine.system() == 'linux'
  # TODO: old kernel support
  _headers += ['linux/magic.h']
endif

# TODO: handle valgrind separately

foreach h : _headers
  config.set10('HAVE_@0@'.format(h.underscorify().to_upper()),
               cc.check_header(h))
endforeach

foreach f : ['FE_ALL_EXCEPT', 'FE_INEXACT']
  config.set10('HAVE_DECL_@0@'.format(f.underscorify().to_upper()),
               cc.has_header_symbol('fenv.h', f))
endforeach

config.set10(
  'HAVE_BUILTIN_THREAD_POINTER',
  cc.compiles('''
    #if _has_attribute(used)
    #define LLVM_ATTRIBUTE_USED __attribute__((__used__))
    #else
    #define LLVM_ATTRIBUTE_USED
    #endif
    LLVM_ATTRIBUTE_USED void *foo() {
      return __builtin_thread_pointer();
    }
    int main(void) { return 0; } ''',
    name : '__builtin_thread_pointer'))

# TODO: APPLE crash reporter

# TODO: not Windows checks
#   Some of these are going to have builtin dependency interactions
if host_machine.system() != 'windows'
  # TODO: pthreads
  deps_system += dependency('dl', required : false)
  dep_rt = dependency('rt', required : false)
else
  dep_rt = dependency('', required : false)
endif
deps_system += dep_rt

# TODO: this is kinda hacky
dep_threads = dependency('threads')

# TODO: FindLibpfm

# TODO: HAVE_LIBPTHREAD

# TODO: check for compress2
dep_zlib = dependency('zlib', required : get_option('zlib'))
config.set10('LLVM_ENABLE_ZLIB', dep_zlib.found())

opt_zstd = get_option('zstd') \
  .disable_auto_if('memory' in get_option('b_sanitize'))
dep_zstd = dependency('libzstd', required : opt_zstd)
config.set10('LLVM_ENABLE_ZSTD', dep_zstd.found())

dep_ffi = dependency('libffi', required : get_option('ffi'))
config.set10('LLVM_ENABLE_FFI', dep_ffi.found())

opt_xml2 = get_option('libxml2') \
  .disable_auto_if('memory' in get_option('b_sanitize'))
dep_xml2 = dependency('libxml-2.0', required : opt_xml2)
config.set10('LLVM_ENABLE_LIBXML2', dep_xml2.found())

dep_curl = dependency('libcurl', required : get_option('curl'))
config.set10('LLVM_ENABLE_CURL', dep_curl.found())

# TODO: ENABLE_HTTPLIB
dep_httplib = dependency('', required : false)

# TODO: SANITIZER + libedit
dep_libedit = dependency('', required : false)

has_logf128 = cpp.has_header_symbol('math.h', 'logf128')
config.set10('HAS_LOGF128', has_logf128)

config.set10('HAVE_DECL_ARC4RANDOM', cpp.has_header_symbol('stdlib.h', 'arc4random'))

# FIXME: Meson probably needs a builtin dependency for this for this
if cc.has_header_symbol('execinfo.h', 'backtrace')
  dep_backtrace = declare_dependency(
    variables : {'header' : 'execinfo.h'}
  )
else
  dep_backtrace = dependency('', required : false)
endif
deps_system += dep_backtrace
# TODO: handle other system

config.set10('HAVE_BACKTRACE', dep_backtrace.found())
config.set('BACKTRACE_HEADER', dep_backtrace.get_variable(internal : 'header'))

# TODO: unguarded-availability-new

# Determine whether we can register EH tables
foreach s : ['register_frame', 'deregister_frame', 'unw_add_dynamic_fde']
  config.set10(
    'HAVE_@0@'.format(s.to_upper()),
    cc.has_header_symbol('cmake/unwind.h', f'__@s@')
  )
endforeach

_symbol_checks = {
  'unwind.h' : ['_Unwind_Backtrace'],
  'unistd.h' : [
    'getpagesize', 'sysconf', 'isatty', 'pread', 'sbrk',
  ],
  'sys/resource.h' : ['getrusage', 'setrlimit'],
  'sys/stat.h' : ['futimens'],
  'sys/time.h' : ['futimes'],
  'malloc_np.h' : ['mallctl'],
  'malloc.h' : ['mallinfo', 'mallinfo2'],
  'malloc/malloc.h' : ['malloc_zone_statistics'],
  'spawn.h' : ['posix_spawn'],
  'string.h' : ['strerror_r', 'strerror_s'],
  # TODO: signalstack
  # TODO: getrlimit
  'stdlib.h' : ['setenv'],
  'libproc.h' : ['proc_pid_rusage'],
}
# TODO: windows

foreach h, _s : _symbol_checks
  foreach s : _s
    config.set10('HAVE_@0@'.format(s.underscorify().to_upper()),
                cc.has_header_symbol(h, s))
  endforeach
endforeach

# TODO: timespec
# TODO: pthread
# TODO: dlfcn
# TODO: find_program(dot)
# TODO: include(CheckAtomic)
# TODO: variadic macros
# TODO: maybe uninitialized
# TODO: no uninitionaled
# TODO: disable old gcc warnings
# TODO: LLVM_INCLUDE_TESTS
# TODO: host-triple

cpu_family = host_machine.cpu_family()
if cpu_family == 'x86'
  cpu_family = 'i686'
endif
if host_machine.system() == 'windows'
  if cc.get_id() in ['msvc', 'clang-cl']  # also Clang on windows
    host_triple = f'@cpu_family@-pc-windows-msvc'
  else
    # TODO: This should only be for mingw and not msys
    host_triple = f'@cpu_family@-w64-windows-gnu'
  endif
# TODO: s390x
elif host_machine.system() == 'aix'
  if cpu_family == 'powerpc64'
    cpu_family = 'powerpc'
  endif
  host_triple = f'@cpu_family@-ibm-aix'
else
  if meson.is_cross_build()
    # We can't run config.guess, since that returns the value for the build
    # machine, not the host machine
    #
    # FIXME: This is almost certainly a complex enough problem that Meson should
    # provide a helper for this.
    # XXX: assuming linux-gnu
    host_triple = f'@cpu_family@-unknown-linux-gnu'
  else
    host_triple = run_command(find_program('sh'), 'cmake/config.guess', check : true).stdout().strip()
  endif
endif
config.set('LLVM_HOST_TRIPLE', host_triple)
summary('LLVM host triple', host_triple)

native_arch = build_machine.cpu_family()
if native_arch in ['x86', 'x86_64']
  native_arch = 'X86'
elif native_arch in ['powerpc', 'powerpc64']
  native_arch = 'PowerPC'
elif native_arch == 'sparc'
  native_arch = 'Sparc'
elif native_arch == 'aarch64'
  native_arch = 'AArch64'
elif native_arch == 'arm'
  native_arch = 'ARM'
else
  # TODO: finish filling this out
  error(f'Unknown architecture @native_arch@')
endif
summary('native architecture', native_arch)

# TODO: NATIVE_KEYWORD loop
#       The allows native and host to be put into target names?

if native_arch in targets_to_build
  config.set('LLVM_NATIVE_TARGET', f'LLVMInitialize@native_arch@Target')
  config.set('LLVM_NATIVE_TARGETINFO', f'LLVMInitialize@native_arch@TargetInfo')
  config.set('LLVM_NATIVE_TARGETMC', f'LLVMInitialize@native_arch@TargetMC')
  config.set('LLVM_NATIVE_ASMPRINTER', f'LLVMInitialize@native_arch@AsmPrinter')

  # We don't have an ASM parser for all architectures yet.
  if fs.exists('lib/Target' / native_arch / 'ASMParser/meson.build')
    config.set('LLVM_NATIVE_ASMPARSER', f'LLVMInitialize@native_arch@AsmParser')
  endif

  # We don't have a disassembler for all architectures yet
  if fs.exists('lib/Target' / native_arch / 'Disassembler/meson.build')
    config.set('LLVM_NATIVE_ASMPARSER', f'LLVMInitialize@native_arch@Disassembler')
  endif
endif

# TODO: if MSVC (winsysroot, dia sdk)
# TODO: threads
# TODO: doxygen
# TODO: gold
# TODO: Apple stuff
# TODO: Bindings
# TODO: python
# TODO: prefixes and suffixes?

# End config-ix

config.set('LLVM_DEFAULT_TARGET_TRIPLE', config.get('LLVM_NATIVE_TARGET', ''))

# TODO: LLVM_ENABLE_PLUGINS
# TODO: finish HandleLLVMOptions
# TODO: generic system, HAVE_LINK_SCRIPT
config.set10('LLVM_ON_WIN32', host_machine.system() in ['windows', 'cygwin'])
config.set10('LLVM_ON_UNIX', host_machine.system() not in ['windows', 'cygwin'])

# TODO: tflite
# TODO: tensorflow

# Configure the thre LLVM configuration header files.
subdir('include/llvm/Config')

# TODO: AIX stuff
# TODO: OS390
# TODO: include dirs
# TODO: cross compile stuff
# TODO: include(AddLLVM)
# TODO: include(TableGen)
# TODO: include(LLVMDistributionSupport)
# TODO: umbrella_lit_testsuite_begin

add_project_dependencies(
  declare_dependency(
    include_directories : include_directories('include')
  ),
  language : ['c', 'cpp'],
)

subdir('lib/Demangle')
subdir('lib/Support')
subdir('lib/TableGen')

# We need llvm-min-tblgen to be able to generate other targets
# CMake apparently allows more out of order resolution here
# TODO: this should be built for the build machine
subdir('utils/TableGen/Basic')

subdir('include')
subdir('lib/CodeGenTypes')
subdir('utils/TableGen')
subdir('lib')
# TODO: include_utils
# TODO: native visualizers to solution
# TODO: bindings
# TODO: projects
# TODO: include_tools
# TODO: include_runtimes
# TODO: include_examples
# TODO: include_tests
# TODO: include_docs
# TODO: cmake/modules?
# TODO: include_utils
# TODO: not toolchain only (might belong in include/)
# TOdO: distrobution_add_Targets
# TODO: MSVC
# TODO: include_benchmarks
# TODO: utils and tools
# TODO: xcode
