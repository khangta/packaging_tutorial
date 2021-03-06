from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-khangta",
    version="0.0.1",
    author="Example Author",
    author_email="truongankhang@gmail.com",
    description="A small example package",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khangta/packaging_tutorial",
    project_urls={
        "Bug Tracker": "https://github.com/khangta/packaging_tutorial/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    # packages=[],
    python_requires=">=3.8",
)