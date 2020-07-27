from setuptools import setup, find_packages
setup(
  name="supported_sats",
  version="0.1",
  packages=find_packages(),
  scripts=["supported_sats.py"],

  install_requires=["pyyaml"]
)

