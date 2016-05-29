from setuptools import setup, find_packages


setup(name="web_app",
      version="1.0",
      entry_points={"paste.app_factory":['sample_factory=app.sample_factory:app_factory']},
      packages=find_packages(),
      )
