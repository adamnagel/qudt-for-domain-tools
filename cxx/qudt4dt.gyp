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
          './src/modelicaUnit.cpp',
          './src/mdaoUnit.cpp',
        ],
        'link_settings': {
            'libraries': [
                '/usr/lib/libjsoncpp.so', '/usr/lib/x86_64-linux-gnu/libcurl.so',
            ],
        },
    },
    {
        'target_name': 'sample',
        'type': 'executable',
        'cflags':['-std=c++11'],
        'dependencies':[
          'libqudt4dt',
        ],
        'include_dirs':[
          './include/',
        ],
        'sources':[
          'sample.cpp',
        ],
        
      },
    ]
  }
