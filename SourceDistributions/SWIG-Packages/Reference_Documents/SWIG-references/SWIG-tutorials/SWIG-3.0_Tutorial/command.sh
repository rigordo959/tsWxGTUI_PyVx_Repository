#!/usr/bin/bash
#"Time-stamp: <08/15/2016  3:03:05 AM rsg>"

function makeSWIG() {
  echo "makeSWIG(" $1 ")"

  swig -python $1.i

  ###########################################################################
  # Excerpt from "SWIG-1.0_Tutorial" / "PyTutorial98.pdf"
  #
  # Interfacing C/C++ and Python with SWIG
  #
  #               David M.  Beazley
  #         Department of Computer Science
  #              University of Chicago
  #             Chicago, Illinois  60615
  #
  #             beazley@cs.uchicago.edu
  #
  ###########################################################################
  #
  # Unfortunately, the build process varies on every machine
  #
  # Solaris
  #
  # cc -c -I/usr/local/include/python1.5 \
  #       -I/usr/local/lib/python1.5/config \
  #        example.c wrapper.c ld -G example.o wrapper.o -o examplemodule.so
  #
  # Linux
  #
  # gcc -fpic -c -I/usr/local/include/python1.5 \
  #       -I/usr/local/lib/python1.5/config \
  #       example.c wrapper.c
  # gcc -shared example.o wrapper.o -o examplemodule.so
  #
  # Irix
  #
  # cc -c -I/usr/local/include/python1.5 \
  #       -I/usr/local/lib/python1.5/config \
  #        example.c wrapper.c
  # ld -shared example.o wrapper.o -o examplemodule.so
  ###########################################################################

  gcc -fpic -c -I/usr/local/include/Python2.7 $1.c $1_wrap.c $1_wrap.c
  gcc -shared $1.o $1_wrap.o -o $1.so
  # tclsh

  # load ./$1.so
  # fact 4
  # 24
  # my_mod 23 7
  # 2
  # expr $My_variable + 4.5
  # 7.5

}

# makeSWIG example
makeSWIG example
