import sys
from lib2to3 import refactor


lib2to3_fix_names = set([
    'lib2to3.fixes.fix_apply',
    'lib2to3.fixes.fix_basestr',
    # 'lib2to3.fixes.fix_buffer',
    # 'lib2to3.fixes.fix_callable',
    'lib2to3.fixes.fix_dict',
    'lib2to3.fixes.fix_except',
    'lib2to3.fixes.fix_exec',
    'lib2to3.fixes.fix_execfile',
    'lib2to3.fixes.fix_exitfunc',
    'lib2to3.fixes.fix_filter',
    'lib2to3.fixes.fix_funcattrs',
    # 'lib2to3.fixes.fix_future',
    'lib2to3.fixes.fix_getcwdu',
    'lib2to3.fixes.fix_has_key',
    'lib2to3.fixes.fix_idioms',
    'lib2to3.fixes.fix_import',
    'lib2to3.fixes.fix_imports',
    'lib2to3.fixes.fix_input',
    'lib2to3.fixes.fix_intern',
    'lib2to3.fixes.fix_isinstance',
    'lib2to3.fixes.fix_itertools',
    'lib2to3.fixes.fix_itertools_imports',
    'lib2to3.fixes.fix_long',
    'lib2to3.fixes.fix_map',
    # 'lib2to3.fixes.fix_metaclass',
    'lib2to3.fixes.fix_methodattrs',
    'lib2to3.fixes.fix_ne',
    'lib2to3.fixes.fix_next',
    'lib2to3.fixes.fix_nonzero',
    'lib2to3.fixes.fix_numliterals',
    # 'lib2to3.fixes.fix_operator',  - what is this?
    'lib2to3.fixes.fix_paren',
    'lib2to3.fixes.fix_print',
    'lib2to3.fixes.fix_raise',
    'lib2to3.fixes.fix_raw_input',
    'lib2to3.fixes.fix_reduce',
    'lib2to3.fixes.fix_renames',
    'lib2to3.fixes.fix_repr',
    'lib2to3.fixes.fix_set_literal',
    'lib2to3.fixes.fix_standarderror',
    'lib2to3.fixes.fix_sys_exc',
    'lib2to3.fixes.fix_throw',
    'lib2to3.fixes.fix_tuple_params',
    'lib2to3.fixes.fix_types',
    'lib2to3.fixes.fix_unicode',
    'lib2to3.fixes.fix_urllib',
    'lib2to3.fixes.fix_ws_comma',
    'lib2to3.fixes.fix_xrange',
    'lib2to3.fixes.fix_xreadlines'
    'lib2to3.fixes.fix_zip'
])

future_package_fix_names = set([
    'libfuturize.fixes.fix_future_package'
    'libfuturize.fixes.fix_metaclass'
    # 'libfuturize.fixes.fix_print'
    # 'libfuturize.fixes.fix_'
    ])
