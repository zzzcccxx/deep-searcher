from setuptools import setup, find_packages

setup(
    name='deeprag',
    version='0.0.1',
    py_modules=['deeprag'],
    packages=find_packages(),
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': ['deeprag=deeprag.cli:main'],
    },
    description='None',
    author='Cheney Zhang',
    author_email='277584121@qq.com',
    url="",  #TODO

)
