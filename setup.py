from setuptools import setup

setup(
    name='ccwc',
    version='1.0.0',
    py_modules=['ccwc'],
    entry_points={
        'console_scripts': [
            'ccwc=ccwc:main', 
        ],
    },
    description='A simple wc implementation for counting bytes in a file.',
    author='Ruby',
    author_email='buihongngoc.hnams@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
