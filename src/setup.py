from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

c_ext = Extension("yolo_utils", sources=["_yolo_utils.c", "yolo_utils.c"])

class BuildExt(build_ext):
    def build_extensions(self):
        self.compiler.initialize()
        self.compiler.initialize_options()
        self.compiler.platform = self.plat_name
        self.compiler.with_msvc_version('14.0')
        build_ext.build_extensions(self)

setup(
    name='yolo_utils',
    version='0.1',
    description='This module provides some basic utilities required for training, evaluating and using a YOLO model in C.',
    ext_modules=[c_ext]
)