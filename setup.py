import ast
import codecs
import os
import re

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description
with codecs.open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()


# Get version
_VERSION_RE = re.compile(r"VERSION\s+=\s+(.*)")

with open("pytest_clickhouse_mock/__init__.py", "rb") as f:
    VERSION = str(ast.literal_eval(_VERSION_RE.search(f.read().decode("utf-8")).group(1)))


setup(
    name="pytest-clickhouse-mock",
    version=VERSION,
    description="",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.everynet.io/platform/libs/pytest-clickhouse-mock",
    author="Alexey Dalekin",
    author_email="alexey.dalekin@everynet.com",
    platforms=["any"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: System :: Distributed Computing",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
    ],
    keywords="pytest clickhouse mock",
    packages=find_packages(exclude=["test*"]),
    setup_requires=["pytest-runner"],
    install_requires=["mock>=3.0.5", "clickhouse_driver>=0.0.16", "pytest>=4.6.5"],
    tests_require=["coverage==4.5.4", "pytest==4.6.5", "pytest-cov==2.7.1"],
    entry_points={"pytest11": ["clickhouse_mock = pytest_clickhouse_mock.plugin"]},
)
