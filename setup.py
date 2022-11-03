import setuptools

with open("README.md", "r") as f:
    readme = f.read()

with open("docs-requirements.txt", "r") as f:
    docs_require = f.read().split("\n")

INSTALL_REQUIRES = [
    "matplotlib",
    "numpy",
    "pandas",
    "Pillow",
]

EXTRAS_REQUIRE = {
    "development": [
        "pytest",
        "black",
    ],
    "docs": docs_require,
}

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"
    "Programming Language :: Python :: 3.9"
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Framework :: Matplotlib",
    "Topic :: Scientific/Engineering :: Visualization",
]

setuptools.setup(
    name="plottable",
    version="0.1.2",
    author="znstrider",
    author_email="mindfulstrider@gmail.com",
    author_twitter="@danzn1",
    description="Beautifully customized tables with matplotlib",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/znstrider/plottable",
    packages=setuptools.find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt"]
    },
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=CLASSIFIERS,
    python_requires=">=3.7",
)
