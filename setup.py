from setuptools import setup
import re

with open('valk2jpg/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

setup(
        name="valk2jpg",
        version=version,
        author="Yehuda Garti",
        author_email="yehuda.garti@intel.com",
        description="Convert Valkyrie bin files to jpg",
        packages=["valk2jpg"],
        python_requires=">=2.7",
        install_requires=[
            'opencv-python>=4.0'
            'numpy',
            ],
        entry_points={
            'console_scripts': [
                'valk2jpg = valk2jpg.__main__:main'
                ]
            }
        )
