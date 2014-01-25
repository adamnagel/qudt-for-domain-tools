 {
    'targets': [
      {
        'target_name': 'libqudt4dt',
        'type': 'static_library',
        'defines': [
          'FOO',
          'BAR=some_value',
        ],
        'include_dirs': [
          './include/',
        ],
        'dependencies': [
        ],
        'direct_dependent_settings': {
        },
        'export_dependent_settings': [
        ],
        'sources': [
          './src/qudt4dt.cpp',
          './src/qudtUnit.cpp',
          './src/sparql.cpp',
        ],
      },
    ],
  }