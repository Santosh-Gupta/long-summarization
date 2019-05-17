
import codecs
from setuptools import setup, find_packages

with codecs.open('README.md', 'r', 'utf8') as reader:
    long_description = reader.read()


with codecs.open('requirements.txt', 'r', 'utf8') as reader:
    install_requires = list(map(lambda x: x.strip(), reader.readlines()))


setup(
    name='long-summarization',
    version='0.01.0',
    packages=find_packages(),
    url='https://github.com/Santosh-Gupta/long-summarization',
    license='MIT',
    author='MedicalQATeam',
    author_email='SanGupta.ML@gmail.com',
    description='BERT in TF2.0 for Medical QA info retrieval + GPT2 for answer generation',
    long_description='None so far',
    long_description_content_taype='text/markdown',
    python_requires = '>=3.6.0',
    #install_requires=['numpy', 'pandas', 'tensorflow-gpu==1.5', 'tabulate', 'pyrouge' ], 
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)




