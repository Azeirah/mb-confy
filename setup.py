"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup

with open("readme.md", "r") as f:
    long_description = f.read()


setup(
    name='mb-confy',

    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.1',

    description='A dictionary backed by a real .json file',
    long_description=long_description,

    url='https://github.com/Azeirah/confy',

    author='Martijn Brekelmans',
    author_email='tijntje_7@msn.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='configuration config json ini',
)
