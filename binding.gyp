{
  "targets": [
    {
      "target_name": "scoring",
      "sources": [ "zxcvbn.cpp" ],
      "cflags_cc": [ "-DNODE_BINDINGS" ],
      "include_dirs": [
        "<!(nodejs -e \"require('nan')\")"
      ]
    }
  ]
}
