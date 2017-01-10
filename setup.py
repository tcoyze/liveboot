# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='liveboot',
    version='0.0.1',
    description='A command line tool for building bootable USBs.',
    author='Tyler Coyner',
    author_email='tyler@tylersbrain.com',
    url='https://github.com/tcoyze/liveboot',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
	'tqdm',
    ],
    entry_points='''
	[console_scripts]
	liveboot=bin.liveboot:cli
    ''',
    license='MIT',
    zip_safe=False,
    keywords='liveboot',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
