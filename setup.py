from setuptools import setup

description = 'Add real HTML punctuation'
long_desc = description

setup(
    name='punctuation',
    version='0.0.1',
    url='https://github.com/honza/punctuation',
    install_requires=[],
    description=description,
    long_description=long_desc,
    author='Honza Pokorny',
    author_email='me@honza.ca',
    maintainer='Honza Pokorny',
    maintainer_email='me@honza.ca',
    packages=['punctuation'],
    scripts=['bin/punctuation'],
)
