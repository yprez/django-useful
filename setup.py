from setuptools import setup, find_packages

setup(
    name='my-package',
    author='Yuri Prezument',
    author_email='y@yprez.com',
    version='0.1.0a0',
    packages=find_packages(),
    license='ISC',
    url='http://github.com/yprez/django-useful',
    description='Reusable Django snippets',
    long_description=open('README.rst').read(),
#    install_requires=[
#    ],
#    classifiers=(
#    ),
)
