#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='audio-stft-processor',
    version='0.1.0',
    author='姜翼顥',
    author_email='example@example.com',
    description='音訊信號的短時傅立葉轉換(STFT)和逆轉換(iSTFT)處理工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Hank-Jiang40815/audio-stft-processor',
    project_urls={
        'Bug Tracker': 'https://github.com/Hank-Jiang40815/audio-stft-processor/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.20.0',
        'scipy>=1.7.0',
        'matplotlib>=3.4.0',
        'soundfile>=0.10.0',
        'librosa>=0.8.0',
        'PyAudio>=0.2.11',
        'tqdm>=4.60.0',
    ],
    entry_points={
        'console_scripts': [
            'audiostft=audio_stft_processor.cli:main',
        ],
    },
)