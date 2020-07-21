import setuptools

_pkg_version = "1.0.0"
_author = "Thomas McGowan"
_author_email = "mcgo0092@umn.edu"
_license = "MIT"
_repo = "https://github.com/galaxyproteomics/fastg2protlib"


setuptools.setup(
    name="fastg2protlib",
    version=f"{_pkg_version}",
    packages=["fastg2protlib"],
    install_requires=["biopython", "lxml", "networkx", "numpy", "pyteomics", "matplotlib"],
    description="FASTG sequences to a protein library",
    author=f"{_author}",
    author_email=f"{_author_email}",
    url="f{_repo}",
    download_url=f"{_repo}/archive/v_{_pkg_version}.tar.gz",
    license=f"{_license}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.6",
)
