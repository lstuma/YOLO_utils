from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

c_ext = Extension("yolo_utils", sources=["_yolo_utils.c", "yolo_utils.c"])

setup(
    name='yolo_utils',
    version='0.1',
    description='Extension providing some basic utilities required for training, evaluating and using a YOLO model in C.',
    ext_modules=[c_ext]
)