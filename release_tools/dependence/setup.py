from setuptools import setup
import os

setup(
    name="tpu_mlir_dependence",
    version=os.getenv("mlir_version").split("-")[0],
    author="sophgo",
    author_email="dev@sophgo.com",
    description=f"Dependence Files of Machine learning compiler based on MLIR for Sophgo TPU {os.getenv('mlir_version')}.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="Apache",
    platforms="unbuntu22.04",
    python_requires=">=3.10,<3.11",
    url="https://github.com/sophgo/tpu-mlir",
    include_package_data=True,
    packages=["tpu_mlir_dependence"],
    keywords=["python3.10", "unbuntu22.04", "linux", "tpu-mlir"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
    ]
)
