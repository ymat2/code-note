from setuptools import setup
from Cython.Build import cythonize

setup(name="cprime", ext_modules=cythonize("cprime.pyx"))
