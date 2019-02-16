"""
    PyByteBuffer
    Copyright (C) 2019  Giovanni Rocca (iGio90)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import PyByteBuffer

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name=PyByteBuffer.__title__,
    version=PyByteBuffer.__version__,

    description='',
    long_description=readme,
    url=PyByteBuffer.__uri__,
    license=PyByteBuffer.__license__,

    author=PyByteBuffer.__author__,
    author_email=PyByteBuffer.__email__,
    python_requires=">=3",
    setup_requires=[],
    install_requires=[],

    packages=[
        "PyByteBuffer",
    ],

    classifiers=[
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
