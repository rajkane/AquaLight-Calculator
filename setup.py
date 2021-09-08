from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
   name='AquaLight-Calculator',
   version='1.0.0',
   description='application for aquarists who need to calculate the optimal lighting for their tanks.',
   license="MIT",
   author='Daniel Torac',
   author_email='daniel.torac@gmail.com',
   url="https://github.com/rajkane/AquaLight-Calculator",
   packages=['AquaLight-Calculator'],
   install_requires=required,
)