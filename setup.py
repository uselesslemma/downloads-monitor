from setuptools import setup, find_packages

setup(
    name="downloads-monitor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'downloads-monitor=monitor.monitor:main',
        ],
    },
    author="Trevor Picard",
    author_email="tpicard+github@proton.me",
    description="A script to monitor downloads and remove duplicates.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/uselesslemma/downloads-monitor",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
