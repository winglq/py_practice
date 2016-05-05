from setuptools import setup, find_packages


setup(name="foo",
      version="2.0",
      entry_points={"console_scripts":['fooc=fd.foo:main']},
      packages=find_packages(),
      )
