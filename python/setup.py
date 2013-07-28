from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(cmdclass={'build_ext': build_ext}, ext_modules=[
    Extension("ad3", ["factor_graph.pyx"], language="c++",
              include_dirs=["../"], libraries=["ad3"])])
