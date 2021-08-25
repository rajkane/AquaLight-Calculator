from setuptools import setup

setup(
   name='AquaLight-Calculator',
   version='0.9',
   description='application for aquarists who need to calculate the optimal lighting for their tanks.',
   license="MIT",
   author='Daniel Torac',
   author_email='daniel.torac@gmail.com',
   packages=['AquaLight-Calculator'],
   install_requires=['PyQt5>=5.15.4'],
)