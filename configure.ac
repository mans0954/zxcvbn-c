AC_INIT([zxcvbn-c],[0.01])
dnl = Do next line i.e. a comment
dnl Library versioning
dnl We begin with 0:0:0
dnl Note, the software release number and library version are independent of eachother
LIB_CURRENT=0
LIB_REVISION=0
LIB_AGE=0
AC_SUBST(LIB_CURRENT)
AC_SUBST(LIB_REVISION)
AC_SUBST(LIB_AGE)
AC_PREREQ([2.68])
AC_CONFIG_MACRO_DIRS([m4])
PKG_INSTALLDIR
AC_CONFIG_SRCDIR([zxcvbn.c])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE([1.11 foreign -Wall -Werror -Wno-extra-portability])
AC_CONFIG_FILES([Makefile libzxcvbn.pc])
AC_PROG_CC
AC_PROG_CXX
LT_INIT
AC_CHECK_LIB([m],[cos])
AC_OUTPUT
