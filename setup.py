"""
Setup script for Python Functions Reference package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="python-functions-reference",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive reference collection of basic Python functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-functions-reference",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[],  # Most functions use standard library only
    extras_require={
        "dev": requirements,
    },
    include_package_data=True,
    zip_safe=False,
)
