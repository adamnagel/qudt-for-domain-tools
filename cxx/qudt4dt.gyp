 {
    'targets': [
      {
        'target_name': 'libqudt4dt',
        'type': 'shared_library',
        'cflags':['-fPIC'],
        'include_dirs': [
          './include/',
        ],
        'sources': [
          './src/qudt4dt.cpp',
          './src/qudtUnit.cpp',
          './src/sparql.cpp',
          './src/modelicaUnit.cpp'
        ],
        'conditions':[
          ['OS=="linux"', {
            'ldflags': [
              '-fPIC',
            ]
           }],
         ]
      },
      {
        'target_name': 'sample',
        'type': 'executable',
        'dependencies':[
          'libqudt4dt',
        ],
        'include_dirs':[
          './include/',
        ],
        'sources':[
          'sample.cpp',
        ],
        'conditions':[
          ['OS=="linux"', {
            'ldflags': [
              '-lcurl',
              '-ljsoncpp',
            ],
          }],
        ],
      },
    ]
  }
