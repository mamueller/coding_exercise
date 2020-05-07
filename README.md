run the profiling by simply by:
python profiling.py

The code is organized in a way to highlight small differences between the different implementations by using 
diff. To compare pcc_forloop_compiled.py and the original python_3.py:
simply say:
diff pcc_forloop_compiled.py python_3.py



It turns out that the original code, although very unpythonic
in its present form is actually higly suited for compilation
(in our case using the numba compiler).
The reason is that it is a 'single sweep' algorythm that
traverses the arrays ONLY ONCE.
This is exactly what vector computers were invented for (then Crays ...today
vector instructions sets for CPUs and GPUs)
The inner part of the original while loop is recognized as a 'compute kernel' 
by modern compilers and fed into the vector registers of modern CPUs or GPUs.
This is the reason why the code is even faster than the highly optimized
numpy functions that also use the vector instructions but EACH traverse the array.

The conclusion is that the code was very likely carelessly copied to python from a compiled language.

Notwithstanding the effective optimization for vector machines it has a numerical stability problem:
The accumulation of the sums leads to overflows for large sample sizes.
Better algorithms would first divide and then sum...
