# Always prefer setuptools over distutils
from setuptools import setup

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="measurement-workbox",
    version="0.0.1",
    description="Library for processing, analyzing, and statistical assessments of measurements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://measurementworkbox.readthedocs.io/",
    author="Matthew M. Willmering",
    author_email="matt.willmering@email.com",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
    ],
    packages=["mw"],
    include_package_data=True,
    install_requires=[""],
)
