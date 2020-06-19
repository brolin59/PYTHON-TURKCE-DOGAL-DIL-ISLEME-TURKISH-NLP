from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='trnlp',
        version='0.2.0a0',
        description='Türkçe doğal dil işleme araçları',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/brolin59/PYTHON-TURKCE-DOGAL-DIL-ISLEME-TURKISH-NLP',
        author='Esat Mahmut Bayol',
        author_email='trnlp2020@gmail.com',
        license='GNU General Public License v3 (GPLv3)',
        classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Intended Audience :: Education',
                'Intended Audience :: Science/Research',
                'Intended Audience :: Information Technology',
                'Environment :: Win32 (MS Windows)',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                'Programming Language :: Python :: 3.7',
        ],
        keywords='türkçe doğal dil işleme araçları nlp ddi',
        packages=find_packages(),
        include_package_data=True,
        python_requires='>=3.5',
        project_urls={
                'Documentation': 'https://github.com/brolin59/PYTHON-TURKCE-DOGAL-DIL-ISLEME-TURKISH-NLP/wiki',
                'Source'       : 'https://github.com/brolin59/PYTHON-TURKCE-DOGAL-DIL-ISLEME-TURKISH-NLP',
        },
)