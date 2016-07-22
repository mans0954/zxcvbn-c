ACLOCAL_AMFLAGS=-I m4

bin_PROGRAMS = zxcvbn-check
zxcvbn_check_SOURCES = test.c 

lib_LTLIBRARIES = libzxcvbn-inline-1.0.la
libzxcvbn_inline_1_0_la_SOURCES = zxcvbn.c dict-src.h zxcvbn.h

include_HEADERS = zxcvbn.h

zxcvbn_check_LDADD = $(lib_LTLIBRARIES)
