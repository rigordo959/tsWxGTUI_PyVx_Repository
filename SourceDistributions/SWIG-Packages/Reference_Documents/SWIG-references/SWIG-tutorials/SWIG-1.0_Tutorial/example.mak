% swig -python example.i
Generating wrappers for Python
% cc -c example.c example_wrap.c \
-I/usr/local/include/python1.5 \
-I/usr/local/lib/python1.5/config
% ld -shared example.o example_wrap.o -o examplemodule.so
