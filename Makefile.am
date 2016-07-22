ACLOCAL_AMFLAGS=-I m4


WORDS = words-10k-pass.txt words-english.txt words-female.txt words-male.txt words-surname.txt

dict-src.h: dictgen $(WORDS)
	./dictgen -o dict-src.h $(WORDS)

dict-crc.h: dictgen $(WORDS)
	./dictgen -b -o zxcvbn.dict -h dict-crc.h $(WORDS)

BUILT_SOURCES = dict-src.h

bin_PROGRAMS = zxcvbn-check dictgen
zxcvbn_check_SOURCES = test.c 
dictgen_SOURCES = dict-generate.cpp
dictgen_CXXFLAGS = -std=c++11

lib_LTLIBRARIES = libzxcvbn-inline-1.0.la
libzxcvbn_inline_1_0_la_SOURCES = zxcvbn.c dict-src.h zxcvbn.h

include_HEADERS = zxcvbn.h

zxcvbn_check_LDADD = $(lib_LTLIBRARIES)
