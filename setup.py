from setuptools import setup, find_packages
from src.torchslime_extensions import __version__

README = 'README.md'

setup(
    name='torchslime_extensions',
    version=__version__,
    packages=find_packages(),
    include_package_data=False,
    entry_points={},
    install_requires=[],
    url='https://github.com/SlimeAI/torchslime_extensions',
    author='SlimeAI',
    author_email='liuzikang0625@gmail.com',
    license='MIT License',
    description='torchslime_extensions',
    long_description=open(README, encoding='utf-8').read(),
    long_description_content_type='text/markdown'
)
