from setuptools import setup, find_packages

setup(
    name='django-useful',
    author='Yuri Prezument',
    author_email='y@yprez.com',
    version='0.1.0',
    packages=find_packages(),
    license='ISC',
    url='http://github.com/yprez/django-useful',
    description='Reusable Django snippets',
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
