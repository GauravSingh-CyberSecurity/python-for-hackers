'''
pip install nuitka
pip install PyInstaller
'''

print("hacked!")


import PyInstaller
import nuitka
import pytoexe

from setuptools import setup

setup(
    name='python-to-exe',
    version='1.0',
    description='Description of your program',
    author='Your Name',
    author_email='your@email.com',
    url='http://www.yourwebsite.com',
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=[{'script': 'python-to-exe.py'}],
    zipfile=None
)






